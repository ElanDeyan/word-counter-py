from pathlib import Path
import click

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
def lines(ctx: click.Context, files: list[Path]):
    output_format: str = ctx.obj["format"]
    format_type = format_type_from_str(output_format)

    files_and_lines: list[dict[str, object]] = []

    for filepath in files:
        with open(filepath, "r") as f:
            files_and_lines.append(
                {"filepath": filepath.as_posix(), "lines_count": len(f.readlines())}
            )

    data = output_formatter(files_and_lines, format_type)

    click.echo(data)
