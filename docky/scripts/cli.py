import click


@click.command()
@click.option(
    '--count',
    default=1,
    help='Number of echos.'
)
@click.argument(
    'file',
    type=click.File('rb')
)
def docky(count, file: click.File):
    for n in range(count):
        click.echo("File: {}".format(file))


@click.command()
@click.option(
    '--count',
    default=1,
    help='Number of greetings.'
)
@click.option(
    '--name',
    prompt='Your name',
    help='The person to greet.'
)
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


@click.group()
def cli():
    pass


@click.command()
def initdb():
    click.echo('Initialized the database')


@click.command()
def dropdb():
    click.echo('Dropped the database')


cli.add_command(initdb)
cli.add_command(dropdb)


if __name__ == '__main__':
    docky()
