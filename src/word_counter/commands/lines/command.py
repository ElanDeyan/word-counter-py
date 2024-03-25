from pathlib import Path
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
    """
    Counts the number of lines in each of FILES, and formats the output based on the specified format type.
    """
    format_type = format_type_from_str(output_format)

    files_and_lines: list[dict[str, object]] = []

    if ctx.obj["stdin"] is not None:
        stdin_output: str = ctx.obj["stdin"].read()

        files_and_lines.append(
            {"filepath": "stdin", "lines": lines_count(stdin_output)}
        )

    for filepath in files:
        with open(filepath, "r") as f:
            file_content = f.read()
            files_and_lines.append(
                {"filepath": filepath.as_posix(), "lines": lines_count(file_content)}
            )

    data = output_formatter(files_and_lines, format_type)

    click.echo(data)
