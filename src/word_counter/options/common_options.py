import functools
from typing import Any, Callable
import click

from src.word_counter.docs.options.output_format_help import OUTPUT_FORMAT_HELP
from src.word_counter.options.format.OutputFormats import OutputFormats


def common_options(f: Callable[..., Any]):
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
