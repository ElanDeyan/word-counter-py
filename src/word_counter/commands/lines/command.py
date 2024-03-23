from pathlib import Path
from typing import TextIO
import click

from src.word_counter.commands.common_options import common_options
from src.word_counter.core.lines_count import lines_count
from src.word_counter.services.options.format.format_type_from_str import (
    format_type_from_str,
)
from src.word_counter.services.options.format.output_formatter import output_formatter


@click.command
@click.pass_context
@click.argument(
    "files",
    type=click.Path(exists=True, path_type=Path, file_okay=True),
    nargs=-1,
)
@common_options
def lines(ctx: click.Context, files: list[Path], output_format: str):
    format_type = format_type_from_str(output_format)

    files_and_lines: list[dict[str, object]] = []

    if ctx.obj["stdin"] is not None:
        stdin_output: TextIO = ctx.obj["stdin"]

        files_and_lines.append(
            {"filepath": "stdin", "lines": lines_count(stdin_output)}
        )

    for filepath in files:
        files_and_lines.append(
            {"filepath": filepath.as_posix(), "lines": lines_count(filepath)}
        )

    data = output_formatter(files_and_lines, format_type)

    click.echo(data)
