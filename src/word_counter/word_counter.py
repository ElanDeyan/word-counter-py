import click

from src.word_counter.commands.size.size import size


@click.group
def cli():
    pass


cli.add_command(size)


if __name__ == "__main__":
    cli()
