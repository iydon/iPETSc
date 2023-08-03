import click


@click.group()
def cli() -> None:
    pass


@cli.command()
def demo() -> None:
    '''Demo'''
    click.echo('Hello world!')
