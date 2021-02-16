Recast Workflow
===============

Recast_workflow is a tool for creating new computation workflow for
running physics analyses. The generated workflows are interpreted by the
`Yadage engine`_ and are stored as .yml files. The package comes with a
command line interface as well as a python library.

Read the documentation `here`_.

See the tutorial `here <TUTORIAL.md>`__.

Also make sure to check out the `FAQ <FAQ.md>`__ if you run into any problems.

To get a quick overview of the code architecture read `here <ARCHITECTURE.md>`__.

This was developed as part of IRIS-HEP fellowship. The full proposal can
be viewed `here <https://iris-hep.org/fellows/vovechkin.html>`__.

Installation
------------

You can use pip to install recast-workflow:

::

   pip install recast-workflow

Recast-workflow was not developed for Windows file systems, so Windows
users are reccomended to work inside a docker image:

::

   docker pull recast/workflow

Development Notes
-----------------

To install and run all tests:

::

   git clone https://github.com/vladov3000/recast_workflow.git
   cd recast_workflow
   python3 -m venv ./venv
   source venv/bin/activate
   source dev_setup.sh
   pip install -e .[test]
   pytest

.. _Yadage engine: https://github.com/yadage/yadage
.. _here: https://recast-wf.readthedocs.io/en/latest/
