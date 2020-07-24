"""CLI group for creating new workflows"""
import click

@click.group(name='make')
def cli():
    """Command group for creating new workflows"""

@cli.command()
@click.option('-w', '--wf-path', type=click.Path(file_okay=True, resolve_path=True))
def new(wf_path):
    if wf_path: print(wf_path)
