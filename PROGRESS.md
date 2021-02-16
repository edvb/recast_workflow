# Progress of IRIS-HEP Research Fellowship

First a summary of the weekly plan proposed:

   - [X] Week 1-2: Learn Madanalysis5(ma5).
   - [X] Week 2-3: Make Ma5 Docker Image.
   - [X] Week 4-5: Implement and test Ma5 Docker Image.
   - [X] Week 6-7: Learn pyhf.
   - [X] Week 8-9: Implement pyhf subworkflow and docker and test.
   - [X] Week 10-11: REANA integration.
   - [X] Week 12: Write documentation.

Below are comprehensive summaries of progress for each week. New progress will appear at the bottom by Friday 11:59pm (PDT) every week.

### Week 1 (June 19):
  - By this point, I was already ahead by a few weeks, since I hard started investigating ma5 early.
  - I had finished running an end-to-end analysis of an interpretation of the tchannel model for one parameter point.
  - The end goal was to run the analysis for the whole "grid" (parameter space) and interpolate the points in between to reproduce a given contur plot
  - This analysis was run manually using madgraph with pythia to generate a showered .hepmc file which was then fed as input to madanalysis5 (ma5)
  - The results from this initial analysis were not comparable to the given ouputs, since the previous researchers were using a more complex ma5 analysis

### Week 2 (June 26):
  - During the investigation, I created an ma5 docker image to develop in, because I had issues setting up my local enviroment for ma5.
  - The docker image would later be integrated into recast-workflow
  - From last week, the goal was to do a full parameter scan using a specific ma5 analysis.
  - To run the specific ma5 analysis, it was necessary to use ma5 expert/recast mode
  - This was a special ma5 option that also required additional packages (delphes, delphesMa5Tune, PAD, PADMa5Tune)
  - Some of these packages were specifically ma5 versions of other packages. e.g. delphes vs. delpesMa5Tune
  - After fixing some compilation issues with the ma5 package manager, I was able to successfully run the analysis and reproduce one point.
  - The next step was to scan the rest of the points (~170 points).
  - I started working on a python script.

### Week 3 (July 3):
  - I used recast-workflow to quickly create a madgraph+pythia workflow and then manually added madanalysis as another stage in this workflow.
  - Since I was trying to automate the process through a workflow, I had to make modifications to the ma5 docker image I was using for development.
  - Using ma5's run/recast card system, I was able to run the docker image automatically - e.g. docker run recast/ma5 -c ma5/bin -R run_card.dat.
  - The run card contained a series of commands that I would normally have to execture manually, but ma5 had a feature that would process them for me.
  - The recast card contained the analysis name I wanted to reuse.
  - The run and recast cards can be found [here](https://github.com/vladov3000/fpd-scanner/blob/master/inputs/ma5_recast_card.dat) and [here](https://github.com/vladov3000/fpd-scanner/blob/master/inputs/ma5_run_card.dat)
  - Once that had been setup, I could copy the ma5 workflow I used for the
  - Workflow found [here](https://github.com/vladov3000/fpd-scanner/blob/master/workflows/fullma5.yml)
  - I used the input madgraph param_card.dat file from the previous point and reproduced its result by running this new workflow.
  - Then, I made a template file for the input param_card
  - Template found [here](https://github.com/vladov3000/fpd-scanner/blob/master/inputs/param_tmpl_mChi_mPhi.dat) (Note in line 32, 33 there are two variables being formatted: `{mChi}` and `{mPhi}`).
  - Then, I wrote a simple python script that for every point, generated an input param_card.dat from the template, ran the ma5 workflow for that input file, and saved the results.
  - The script is [here](https://github.com/vladov3000/fpd-scanner/blob/master/cl_scanner.py)
  - I also repurposed this scanner to scan for decay and cross-section instead of confidence limits to validate an assumption about madgraph computing the decay-width the same was as the original researchers did.
  - Decay/xsection script [here](https://github.com/vladov3000/fpd-scanner/blob/master/pb_decay_scanner.py)
  - The whole scan took about 72 hours running on my computer without any parallelisation.
  - From [these results](https://github.com/vladov3000/fpd-scanner/tree/master/outputs/folders), I was able to produce a plot that matched closely to the given one.

### Week 4 (July 10):
  - This is the week where I started applying knowledge form the prior weeks to building recast-workflow.
  - The docker image was fully implemented, so I could just copy the files needed to build the image to recast-workflow.
  - For the workflow, I had to cut out the ma5 stage and put it in a seperate file.
  - The way subworkflows are defined in recast-workflow requires that there is also a description.yml file for the ma5 that describes the input/output file interfaces and a common_inputs.py file for determining common inputs for the subworkflow (common inputs refers to inputs that are common among multiple subworkflows, not frequently inputted values).
  - After defining these extra files so recast-workflow can understand the subworkflow, I was able to generate a new end-to-end ma5 workflow (from input cards for generation of data from madgraph to confidence limits in madnalysis5).
  - The files defining the ma5 subworkflow can be found [here] (https://github.com/vladov3000/recast_workflow/tree/master/src/recast_workflow/subworkflows/analysis/madanalysis).
  - With this yadage workflow, I was able to start working with REANA.
  - I had to use ssh tunneling with a vnc to open reana.cern.ch and get my access token.
  - Then in lxplus, I submitted some hello world tutorial REANA jobs that introduced me to the reana.yml file that specified how to run the job and how to get my outputs.
  - I then found a more specific [tutorial](https://awesome-workshop.github.io/reproducible-analyses/) for my use case that was about using REANA with the yadage engine.
  - Using this tutorial, I was able to create a job for my ma5 workflow and scan through all the input cards. This was significantly faster than the python script due to the parallelisation of execution in REANA.
  - I got the same results and was able to reuse my code to recreate the contour plot.
  - After gaining familiarity with running these scans (through python scripts or REANA), I could start implementing features in recast-workflow.
  - First, I made a command (`recast-cli scan build workflow.yml`).
  - This would convert a single input workflow (such as the original ma5 workflow) to a workflow that could take several input files.
  - Then, I added a command to get a directory with your workflow and reana.yml, such that you could copy your inputs into the directory and submit it without any extra modifications.
  - The idea was to also use REANA as a backend for running these workflows that way you could submit using recast-cli, but this is tricky to implement and not very useful for a few reasons.

### Week 5 (July 17):
  - This week was dedicated to learning about pyhf and cleaning up the project, which had gotten bloated with random files.
  - The previous setup had recast-workflow nested in recast-cli, the command line interface for workflow.
  - Due to this setup, a setup script was required to set the `$PYTHONPATH` enviromental variable (points to where python can search for modules).
  - There were also very many complexities with the packageging of recast-cli, since there are many non-.py files that had to be included.
  - This is why I decided to reorganize the project by copying in folders one at a time from recast-workflow. Currently, recast-cli has not been fully integrated yet, but recast-workflow only fails one test.
  - I also changed recast-workflow to be an installable package - this allows for a non-command line python interface with the package (e.g. `import recast_workflow`).
  - It also makes the installation quite simply by only requiring the command `pip install -e .[test]` to start developing.
  - The goal by the end of this project is to build and upload everything, so anyone can install the package just by running `pip install recast-workflow`.
  - With pyhf, I was able to convert a HistFitter analysis workspace to pyhf and do a basic fit.
  - This was done for the MonoJet analysis to reproduce its results as well as for a simple single-bin example. The githubs repos are [here](https://github.com/vladov3000/HistToPyhf) and [here](https://github.com/vladov3000/pyvshf).
  - I am ready to start pyhf integration into recast-workflow and focus on reworking recast-workflow through better organization and more unit tests

 ### Week 6 (July 24):
  - I added back the command line interface component to recast-workflow
  - Found at https://github.com/vladov3000/recast_workflow/tree/master/src/recast_workflow/cli
  - This includes the `recast-wf make new` command that creates a new workflow using an interactive input process from the user
  - The make new command also takes command line arguements that can be substituted in for user input, such that the whole process of making a new workflow can be run without interaction
  - This is useful for a potential backend of a website that provides a UI for making these workflows, so the backend can just run the command with comprehensive arguments for any requests
  - Furthermore, I reimplemented the inventory system (renamed from catalogue).
  - Before, the 'catalogue' in recast-workflow was ambigious. Now, the catalogue is just a list of all the possible workflows for the given filters which the user can pick from. While the inventory is a cache of these generated workflows that can be accessed from any directory on the user's machine.
  - This puts the rework of recast-workflow to about 90% of what it was before the research fellowship began
  - All that is left is adding get_dir (which returns a directory with a run script for executing the workflow) and miscellaneous functions for the inventory
  - Then, the newer features can be copy-pasted and tested more thoroughly with the new system.
  - The subworkflow specifications for pyhf are complete (description.yml, common_inputs.py, workflow.yml), but the docker image is incomplete. The [python script](https://github.com/vladov3000/recast_workflow/blob/master/src/recast_workflow/images/pyhf/make_patch.py) that is the entrypoint for the pyhf docker image currently does nothing with the given arguements.
  - Currently, I have been implementing [my own CL calculator](https://github.com/vladov3000/learncls/blob/master/s5.1-counting-expirement.ipynb) using this [paper](https://arxiv.org/pdf/1007.1727.pdf). Pyhf uses the same approximate formulas, so I should get a better understanding of the pyhf source code and how to find the cls using pyhf.
  - Then, I can finish the pyhf scipt next week and the CL calculator will also be done by Wednesday next week.

### Week 7 (July 31):
  - I finished the rest of the 'base' command line features this week.
  - `recast-wf inv add/getyml/getdir` now work.
  - The inventory works as a glocal storage for workflows generated/used by recast-workflow.
  - `add` will add a workflow to the inventory at a local path. This will be useful later when the scan build feature is copied back in. This would allow users to take a workflow too complex for recast-wf to make, and convert it to a multistage workflow (allowing for parameter scans and parallelisation using REANA).
  - `getyml` will print the workflow text or give a yaml file with the workflow. Since recast-wf automatically replaces all references to other files in the main workflow file, the whole workflow can be stored in one yaml file.
  - `getdir` will produce a directory which includes some extra files/folders to organize the process of running the workflow. For example, it includes a run script which is used as an alias so users don't have to type in the full command to run a yadage workflow with the right arguments (`yadage-run workdir $WORKFLOW inputs/input.yml -d initdir=$PWD/inputs` -> `./run.sh`). All the extra files are stored in a templates folder which can be easily modified to include new files.
  - There are still some complexities with pyhf which require more investigation. Specifically, how .yoda files translate to pyhf JSON histograms.
  - I have also begun working on documentation by writing the introduction of the first tutorial (this will later be moved to a readthedocs.io page): https://github.com/vladov3000/recast_workflow/blob/master/TUTORIAL.md
  - There will also be a summer workshop soon where we want to present recast-workflow, so we have been brainstorming more ideas of applications of recast.
  - I have also been reading through a paper on statistics in physics and constructing a presentation concurently that can be used to explain the analysis/statistic subworkflows well to new students/users.

 ### This document was replaced by weekly meetings.




