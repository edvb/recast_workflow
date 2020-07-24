""" The recast workflow command line interface. """
from .cli import recast_wf as cli
from .complete import cli as complete
from .make import cli as make

# make cli scripts part of recast_workflow.cli.*
__all__ = ['recast-wf', 'complete', 'make']
