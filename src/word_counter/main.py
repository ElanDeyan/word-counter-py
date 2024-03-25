import sys
import click

from src.word_counter.commands.scan.command import scan
from src.word_counter.commands.chars.command import chars
from src.word_counter.commands.lines.command import lines
from src.word_counter.commands.size.command import size
from src.word_counter.commands.words.command import words


@click.group
def cli():
    """
    CLI tool to run a COMMAND with files as ARGS (or from stdin like `cat`) and outputs the result.
    Based in unix's `wc` tool.
    """
    click.get_current_context().obj = {"stdin": None}

    if not sys.stdin.isatty():
        stdin_output = sys.stdin
        click.get_current_context().obj["stdin"] = stdin_output


cli.add_command(size)
cli.add_command(lines)
cli.add_command(words)
cli.add_command(chars)
cli.add_command(scan)

if __name__ == "__main__":
    cli()
