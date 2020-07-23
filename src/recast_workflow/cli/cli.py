import click

from . import complete

@click.group(context_settings=dict(help_option_names=['-h', '--help']))
def recast_wf():
    """ Command-line interface for recast-workflow. """

recast_wf.add_command(complete.cli)
