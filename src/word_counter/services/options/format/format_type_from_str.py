import click
from src.word_counter.options.format.OutputFormats import OutputFormats


def format_type_from_str(format_: str) -> OutputFormats:
    """
    The function `format_type_from_str` converts a string to an `OutputFormats` enum and raises an
    exception if the format is unknown.

    :param format_: The `format_` parameter is a string representing a format type that needs to be
    converted to an `OutputFormats` enum. The function attempts to convert the string to the
    `OutputFormats` enum, and if it fails due to a `ValueError`, it raises a
    `click.exceptions.BadParameter
    :type format_: str
    :return: an instance of the `OutputFormats` class with the format_ argument passed to its
    constructor.
    """
    try:
        return OutputFormats(format_)
    except ValueError:
        raise click.exceptions.BadParameter("Unknown format type.")
