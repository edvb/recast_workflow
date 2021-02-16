# RECAST_workflow Architecture Overview

* pip install workflow runs setup.py with setup.cfg
  * setup.py allows optional dependencies to be installed
    * TODO: need to add docker for dev
  * console used to add exec
* MANIFEST.in includes non python files to module
  * Include for single file
  * Graft for recursive include
* dev_setup.sh
  * Remove python cache
  * Need docker username and password
* src
  * Need `__init__.py` for python to recognize folder
    * Can also run code
    * Use `__main__` and import . to get public objects
  * catalogue.py
    * Gets combo of subworkflows for “make new”
    * Could be rewritten but very hard
  * definitions.py
    * Paths of files when installed to site packages folder
  * inventory.py
    * Global access to workflows
    * Maybe delete get_wf_path
    * TODO able to get workflows from github
  * scan.py
    * Auto gen REANA specifies files
      * TODO not working
    * Multistep workflows for multiple parameters
    * Should merge back to single folder
  * utils.py
    * General utilities
  * workflow.py
    * Build workflows
    * common_inputs.yml
    * Different subworkflows use same input file
* CLI
  * Used to automate setting pythonpath and setting everything up
  * Was used to wrap workflow with command arguments with click
  * Click group for 2nd arg in CLI eg inv, scan
  * Click converts underscores in names to hyphens
  * New files for new groups and add to cli.py and `__main__` in `__init__.py`
  * Complete used for bash to autocomplete with tab
  * Running CLI should be same as using python
    * Should be 1 line in CLI part
  * Arguments are required, options are optional
    * Arguments don't have help messages
  * Docstrings are help message
    * Should mention arguments in caps
  * Click options
    * click.PATH stuff
    * 3rd option if function is reserved
  * In import assume pkg already installed
* Images
  * Builds docker images for dev
  * docker build -t recast/myimagename .
  * ufotar should contain model but does not work currently
* Interfaces
  * Descriptions of files
* Subworkflows
  * Written in YML files
  * Need to implement madgraph options inputs
* Templates
  * Used by getdir to get folder
  * TODO Auto fill input.py from subworkflows interfaces
