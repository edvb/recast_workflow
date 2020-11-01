#!/bin/sh

# get directory of workflow
DIR=$(dirname "$0")
# workflow to run, defaults to workflow.yml if no argument is given
WORKFLOW=${1:-$DIR/workflows/workflow.yml}

rm -r $DIR/workdir
yadage-run $DIR/workdir $WORKFLOW $DIR/inputs/input.yml -d initdir=$PWD/$DIR/inputs
