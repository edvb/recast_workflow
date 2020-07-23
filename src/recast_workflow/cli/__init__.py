""" The recast workflow command line interface. """
from .cli import recast_wf as cli
from .complete import cli as complete

# make cli scripts part of recast_workflow.cli.*
__all__ = ['recast-wf', 'complete']
