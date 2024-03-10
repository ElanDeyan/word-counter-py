import os
from pathlib import Path
import click

from src.word_counter.services.options.format.format_type_from_str import format_type_from_str
from src.word_counter.services.options.format.output_formatter import output_formatter


@click.command
@click.pass_context
@click.argument(
    "files", type=click.Path(exists=True, path_type=Path, file_okay=True),
    nargs=-1
)
@click.option(
    "--ignore-line-sep", is_flag=True, default=False, show_default=True, type=bool
)
def chars(ctx: click.Context, files: list[Path], ignore_line_sep: bool):
    output_format: str = ctx.obj["format"]
    format_type = format_type_from_str(output_format)

    files_and_chars: list[dict[str, object]] = []

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip(os.linesep) if ignore_line_sep else f.read()
            files_and_chars.append({ "filepath": filepath.as_posix(), "char_count": len(content) })
    
    data = output_formatter(files_and_chars, format_type)

    click.echo(data)
