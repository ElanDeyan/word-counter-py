import functools
from typing import Any, Callable
import click

from src.word_counter.docs.options.output_format_help import OUTPUT_FORMAT_HELP
from src.word_counter.options.format.OutputFormats import OutputFormats


def common_options(f: Callable[..., Any]):
    """
    The function `common_options` adds a common command line option for specifying output format to a
    given function.

    :param f: Callable[..., Any]
    :type f: Callable[..., Any]
    :return: The `common_options` function is returning a new function that wraps the original function
    `f` with additional options defined in the `options` list. The additional option being added is for
    specifying the output format, with default value set to `OutputFormats.PLAINTEXT.value`.
    """
    options = [
        click.option(
            "--format",
            "output_format",
            type=click.Choice(OutputFormats.values(), case_sensitive=False),
            default=OutputFormats.PLAINTEXT.value,
            show_default=True,
            help=OUTPUT_FORMAT_HELP,
        ),
    ]
    return functools.reduce(lambda x, opt: opt(x), options, f)
