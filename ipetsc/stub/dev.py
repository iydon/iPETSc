import importlib

import click


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('-u', '--username', default='iydon', show_default=True)
@click.option('-p', '--password', prompt=True, hide_input=True)
def publish(*args, **kwargs) -> None:
    '''Publish iPETSc to pypi.org'''
    importlib.import_module('..command.publish', __package__).api(*args, **kwargs)
