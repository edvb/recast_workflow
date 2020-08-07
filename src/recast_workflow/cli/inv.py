""" Command group for recast-workflow inventory """
import click
import time
import os

import recast_workflow.inventory as inventory

@click.group(name='inv')
def cli():
    """ Command group for interacting with recast-workflow inventory """

@cli.command()
def ls():
    """ List all workflows in inventory """
    li = inventory.list_inv()
    if not li:
        print('No workflows in inventory.')
        return

    fmt = '{0:40}{1:40}'
    click.echo('-' * 80)
    click.echo(fmt.format("WORKFLOW NAMES", "TIME LAST MODIFIED"))
    click.echo('-' * 80)
    for wf in li: click.echo(fmt.format(wf, time.ctime(os.path.getmtime(inventory.get_inv_wf_path(wf)))))

@cli.command()
@click.option('--all', metavar='rm_all', is_flag=True, help='Remove all workflows in inventory.')
@click.option('-f', '--force', is_flag=True, help='Do not ask for confirmation before removing.')
@click.argument('names', nargs=-1)
def rm(names, rm_all, force):
    """ Remove workflows with names NAMES from inventory """

    def confirm() -> bool:
        """ Ask for confirmation before removing """
        if force: return True
        toRm = "all" if rm_all else ' '.join(names)
        return click.confirm('Are you sure you would like to delete {toRm} workflows in inventory?', abort=True)

    if rm_all:
        if not force and not confirm(): return
        for n in inventory.list_inv():
            inventory.remove(n)
    elif confirm():
        for n in names: inventory.remove(n)

@cli.command()
@click.option('-n', '--name', type=str, help='Set name in inventory')
@click.argument('path', type=click.Path(exists=True))
def add(path, name):
    """ Add workflow in .yml file at PATH to inventory. """

    inventory.add(path, name)

@cli.command()
@click.argument('name', type=str)
@click.option('-o','--output-path', type=click.Path(file_okay=True, resolve_path=True), help='Path to output found workflow to.')
def getyml(name, output_path):
    """ Get text of workflow from inventory. """

    res = get_inv_wf_yml(output_path, text=True)
    if not output_path: print(res)

@cli.command()
@click.argument('name', type=str)
@click.argument('output-path', type=click.Path(file_okay=True, resolve_path=True))
def getdir(name, output_path):
    """ Get directory with run script, inputs folder, and workflow """
    inventory.get_dir(name, output_path)
