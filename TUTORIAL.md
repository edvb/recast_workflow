# Recast-workflow Tutorial

## Setup
Ensure python >= 3.6 is installed. It is reccomended to run in a virtual enviroment, so create and source a new python venv.

    python -m venv ./venv
    source ./venv

Now, you can install recast-workflow through pip:

    git clone https://github.com/vladov3000/recast_workflow.git
    pip install ./recast_workflow

## Introduction

This is a temporary markdown file for the tutorial, the full text will be moved to a readthedocs later.

The goal of this tutorial is to replicate the results from [this workshop](https://smeehan12.github.io/2019-08-12-dmatlhc-tutorial/index.html). In this workshop, the process is shown for how to do a search for a dark matter signal in a simple benchmark model shown below. [Talk About Model some more] 

The process consisted of 4 steps:
  1. madgraph for generating detector events (producing a .lhe file)
  2. feeding the .lhe file to pythia to shower the jets and produce a full list of stable hadrons (stored in a .hepmc file)
  3. giving rivet the .hepmc to run selection on and identify the background signal (producing a .yoda file with the results)
  4. then using contur to run some statistical analysis on the .yoda file and produce analyzable plots
 
 All of these steps were done in one docker container with a local directory mounted to the container so the results could be extracted. The idea behind yadage engine is to automate the execution of these instructions. These instructions are represented by yadage workflows - .yml files that follow a schematic defined by yadage. The motivation behind recast-workflow is too automate the generation of these workflows for simple physics analyses like the example above.
 
 To do this, recast-workflow divides an analysis into 3 steps: generation, selection, analysis/statistics. Then, you can choose a subworkflow (a component that will be combined with others to produce the final workflow) for every step. In this example, we are using madgraph+pythia, rivet, and contur for generation, selection, and statistics, respectively. Madgraph and pythia are combined as one subworkflow, since both are necessary to produce the showered data. 
 
 ## Creating a New Workflow
 
 You can start making a new workflow using `recast-workflow make new`. Without any options, this command will run interactively and you will have to fill out all the relevant fields for your workflow. Alternatively, you can specify options for the corresponding input fields and the command will skip asking for user inputs. It is possible to generate the workflow non-interactively just through command line arguments using the '-x' option (will no ask for any user input). After you run the make new command, the utput should look like this (the order of the combinations may be different):
 
    --------------------------------------------------
    Combination 1:
    STEP                NAME                          
    generation          madgraph_pythia               
    analysis            madanalysis                   
    --------------------------------------------------
    Combination 2:
    STEP                NAME                          
    generation          madgraph_pythia               
    selection           rivet                         
    statistics          pyhf                          
    --------------------------------------------------
    Combination 3:
    STEP                NAME                          
    generation          madgraph_pythia               
    selection           rivet                         
    statistics          contur                        
    --------------------------------------------------

    Add an additional common input or enter 'done' to continue: 
 
When you first run the command, you will see all the possible workflow combinations and a prompt asking for common inputs. A subworkflow defines what common inputs are valid and then the command will filter for workflows that accept this input. You can find a list of the available common inputs by running `recast-wf make inputs`. In our case, we are interested in reusing an analysis with inspire ID of ATLAS_2016_I1458270. Enter `analysis_id=ATLAS_2016_I1458270`. After adding this common input, your output should look like this:

    --------------------------------------------------
    Combination 1:
    STEP                NAME                          
    generation          madgraph_pythia               
    selection           rivet                         
    statistics          pyhf                          
    --------------------------------------------------
    Combination 2:
    STEP                NAME                          
    generation          madgraph_pythia               
    selection           rivet                         
    statistics          contur                        
    --------------------------------------------------
    Current common inputs used:
        analysis_id=ATLAS_2016_I1458270

    Add an additional common input or enter 'done' to continue:

From this example, we can see that the madanalysis5 workflow was filtered out. This is because recast is the only subworkflow that accepts the analysis id as a valid common input. Now, we can continue (enter done or just press enter) and select a combination. Select the combination with contur used as statistics and save it to inventory. Show the workflow to see how it looks like, so we can compare against the file we retrieve later.  

Note: If you wanted to get the workflow directly to a .yml file you can use the `-o` or `--output-path` option when running `recast-wf make new`.

 ## Running a New Workflow
 
The workflow is now stored in the inventory. The purpose of the inventory is for you to be able to retrieve this workflow quickly from whatever filepath you are at. You can add, remove, and list workflows in the inventory with the `recast-wf inv add PATH`, `recast-wf inv rm NAME`, and `recast-wf inv ls` commands, respectively. Check our workflow is saved in the inventory using the list command. You should see a workflow with the name `madgraph_pythia-rivet-contur` in the inventory.  

Now, we can retrieve a directory with our workflow  we can fill in with our inputs. Run `recast-wf inv getdir madgraph_pythia-rivet-contur .`. This will produce a new directory in your current directory(`.`). `cd` into this directory to start using it. Inside this directory, you should see these folders/files:
    
    inputs		run.sh		workflows
    
The `workflows` folder has a file called `workflow.yml` that contains the full workflow we previously generated. `run.sh` is just a quick run script for the analysis. Otherwise, you would have to type in the full yadage command to run the workflow:

    yadage-run workdir workflows/workflow.yml inputs/input.yml -d initdir=$PWD/inputs

The input folder contains all your input files as well as an input.yml file that maps the input names to their values. We will require an input file, so in the `inputs` folder create a new file called `proc_card_dm.dat`. In this file, we will write the madgraph process we will be using:

        import model DMsimp_s_spin1 --modelname
        generate p p > xd xd~ j

Then, open `inputs/input.yml` in a text editor. The contents of the file should look like this:

      analysis_id: null
      n_events: null
      proc_card: null
 
 These are all the inputs required to run the workflow, and recast-wf automatically fills in the names of the inputs for you. Now, you just have to fill in the values. In our case, the Inspire id we are using is `ATLAS_2016_I1458270`, 1000 events should be ok, and the filepath to the proccess card is relative to the initdir argument passed to yadage-run (`inputs` folder here). Then, you can run the analysis (without any errors) using `bash run.sh`. The outputs for each step will be in `workdir` once yadage is done running.
 
 ## List of Commands to Run Tutorial

    # Setup
    mkdir rwf_analysis
    cd rwf_analysis
    python3 -m venv ./venv
    source ./venv
    git clone https://github.com/vladov3000/recast_workflow.git
    pip install ./recast_workflow
    
    
    # Creating workflow
    recast-wf make new
    # Add common input by typing analysis_id=1458270 then enter done
    # Select combination using contur for statistics step
    # Save to inventory
    recast-wf inv ls
    recast-wf inv getdir madgraph_pythia-rivet-contur .
    cd madgraph_pythia-rivet-contur
    
    # Add inputs and run for one point
    cd inputs
    vim proc_card_dm.dat 
    # Using a text editor write the following madgraph process:
        import model DMsimp_s_spin1 --modelname
        generate p p > xd xd~ j
    vim input.yml
    # Using a text editor, specify inputs:
        proc_card: 'proc_card_dm.dat'
        n_events: 1000
        analysis_id: ATLAS_2016_I1458270
    cd ..
    ./run.sh
    
    # Create and run a scan
    recast-wf scan build -n madgraph_pythia-rivet-contur proc_card | less # if you just want to check out the output yml
    recast-wf scan build -n madgraph_pythia-rivet-contur -i proc_card
    recast-wf inv ls # Confirm multi_madgraph_pythia_rivet_contur is present
