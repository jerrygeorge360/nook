import click
from nook import commands


@click.group()
@click.version_option("v0.1", prog_name="nook")
def cli():
    pass


cli.add_command(commands.add)
cli.add_command(commands.getvalue)
cli.add_command(commands.delete)


if __name__ == '__main__':
    cli()
