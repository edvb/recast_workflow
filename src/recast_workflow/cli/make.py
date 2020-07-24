"""CLI group for creating new workflows"""
import click

from recast_workflow import catalogue

@click.group(name='make')
def cli():
    """Command group for creating new workflows"""

@cli.command()
@click.option('-w', '--wf-path', type=click.Path(file_okay=True, resolve_path=True))
def new(wf_path):
    # user filters combinations by adding common inputs
    done_adding_ci = False
    ci_used = {}

    while not done_adding_ci:
        combos = catalogue.get_valid_combinations(ci_used)
        if len(combos) < 1: click.secho('No valid combinations for given common inputs')

        # display all valid combinations
        for index, combo in enumerate(combos):
            click.secho('-' * 50)
            click.secho(f'Combination {index + 1}:')
            fmt = '{0:20}{1:30}'
            click.secho(fmt.format('STEP', 'NAME'))
            for k, v in combo.items(): click.secho(fmt.format(k, v))
        click.secho('-' * 50)

        # display current common inputs
        if ci_used != {}: click.secho('Current common inputs used:')
        for k, v in ci_used.items(): click.secho(f'\t{k}={v}')
        click.secho()

        # check to add another common input
        ci_to_add = click.prompt("Add an additional common input or enter 'done' to continue", type=str)

        # check if user is done adding ci
        if ci_to_add == '' or ci_to_add.lower() == 'done':
            done_adding_ci = True
            break

        # Parse input for common input key and value
        ci_to_add = ci_to_add.split('=')
        if len(ci_to_add) == 2:
            ci_used[ci_to_add[0]] = ci_to_add[1]
        else:
            click.secho('Common input not recognized.')

    click.confirm('Do you want to start the "make" process?', abort=True)
