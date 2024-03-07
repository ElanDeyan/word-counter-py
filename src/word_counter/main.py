import click

from src.word_counter.commands.lines.command import lines
from src.word_counter.commands.size.command import size
from src.word_counter.commands.words.command import words


@click.group
def cli():
    pass


cli.add_command(size)
cli.add_command(lines)
cli.add_command(words)


if __name__ == "__main__":
    cli()
