# Recast-workflow Tutorial

# Setup
Ensure python >= 3.6 is installed. It is reccomended to run in a virtual enviroment, so create and source a new python venv.

    python -m venv ./venv
    source ./venv

Now, you can install recast-workflow through pip:

    pip install recast-workflow

# Introduction

This is a temporary markdown file for the tutorial, the full text will be moved to a readthedocs later.

The goal of this tutorial is to replicate the results from [this workshop](https://smeehan12.github.io/2019-08-12-dmatlhc-tutorial/index.html). In this workshop, the process is shown for how to do a search for a dark matter signal in a simple benchmark model shown below. [Talk About Model some more] 

The process consisted of 4 steps:
  1. madgraph for generating detector events (producing a .lhe file)
  2. feeding the .lhe file to pythia to shower the jets and produce a full list of stable hadrons (stored in a .hepmc file)
  3. giving rivet the .hepmc to run selection on and identify the background signal (producing a .yoda file with the results)
  4. then using contur to run some statistical analysis on the .yoda file and produce analyzable plots
 
 All of these steps were done in one docker container with a local directory mounted to the container so the results could be extracted. The idea behind yadage engine is to automate the execution of these instructions. These instructions are represented by yadage workflows - .yml files that follow a schematic defined by yadage. The motivation behind recast-workflow is too automate the generation of these workflows for simple physics analyses like the example above.
 
 To do this, recast-workflow divides an analysis into 3 steps: generation, selection, analysis/statistics. Then, you can choose a subworkflow (a component that will be combined with others to produce the final workflow) for every step. In this example, we are using madgraph+pythia, rivet, and contur for generation, selection, and statistics, respectively. Madgraph and pythia are combined as one subworkflow, since both are necessary to produce the showered data. You can generate this new workflow using `recast-workflow make new`
