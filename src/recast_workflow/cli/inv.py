""" Command group for recast-workflow inventory """
import click
import time

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
    for wf in li: click.echo(fmt.format(wf), time.ctime(os.path.getmtime(inventory.get_inv_wf_path(wf))))

@cli.command()
@click.option('--all', metavar='rm_all', is_flag=True, help='Remove all workflows in inventory.')
@click.option('-f', '--force', is_flag=True, help='Do not ask for confirmation before removing.')
@click.argument('names', nargs=-1)
def rm(names, rm_all, force):
    """ Remove workflow from inventory """

    def confirm() -> bool:
        """ Ask for confirmation before removing """
        if force: return True
        return click.confirm('Are you sure you would like to delete all workflows in inventory?', abort=True)

    if rm_all:
        if not force and not confirm(): return
        for n in inventory.list_inv():
            inventory.remove(n)
    elif confirm():
        for n in names: inventory.remove(n)

@cli.command()
@click.argument('path')
@click.option('-n', '--name', type=str, help='set name in inventory')
def add(path, name):
    """ Add workflow at PATH to inventory. """
