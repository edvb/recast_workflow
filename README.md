# Recast Workflow

Recast_workflow is a tool for creating new computation workflow for running physics analyses. The generated workflows are interpreted by the [Yadage engine](https://github.com/yadage/yadage) and are stored as .yml files. The package comes with a command line interface as while as a python package.

This is currently being developed as part of IRIS-HEP fellowship. The full proposal can be viewed [here](https://iris-hep.org/fellows/vovechkin.html). The current status of the fellowship can be read [here](https://github.com/vladov3000/recast_workflow/blob/master/PROGRESS.md).

## Development Notes

These will be moved to documentation later but for now, they will be here. To install and run all tests:

    git clone url
    cd recast_workflow
    python3 -m venv ./venv
    source venv/bin/activate
    source dev_setup.sh
    pip install -e .[test]
    pytest
    
Expected test results:

    latform darwin -- Python 3.7.7, pytest-3.10.1, py-1.9.0, pluggy-0.13.1
    rootdir: /Users/vlad/Documents/EPEprojects/recast_workflow, inifile:
    collected 37 items                                                                                                          

    tests/images/test_build_utils.py .........                                                                            [ 24%]
    tests/images/test_builds.py .                                                                                         [ 27%]
    tests/scripts/test_catalogue.py ..............                                                                        [ 64%]
    tests/scripts/workflow/test_workflow.py ..s...FF.                                                                     [ 89%]
    tests/subworkflows/selection/test_rivet.py ....                                                                       [100%]

