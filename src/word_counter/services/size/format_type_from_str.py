import click
from src.word_counter.commands.size.OutputFormats import OutputFormats


def format_type_from_str(format_: str) -> OutputFormats:
    try:
        return OutputFormats(format_)
    except ValueError:
        raise click.exceptions.BadParameter("Unknown format type.")
