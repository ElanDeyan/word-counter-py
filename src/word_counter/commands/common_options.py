import functools
from typing import Any, Callable
import click

from src.word_counter.options.format.OutputFormats import OutputFormats


def common_options(f: Callable[..., Any]):
    options = [
        click.option(
            "--format",
            "output_format",
            type=click.Choice(OutputFormats.values(), case_sensitive=False),
            default=OutputFormats.PLAINTEXT.value,
            show_default=True,
        ),
    ]
    return functools.reduce(lambda x, opt: opt(x), options, f)
