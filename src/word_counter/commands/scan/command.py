from pathlib import Path
import click

from src.word_counter.core.char_count import char_count
from src.word_counter.core.filesize import filesize
from src.word_counter.core.lines_count import lines_count
from src.word_counter.core.words_count import words_count
from src.word_counter.services.options.format.output_formatter import output_formatter
from src.word_counter.utils.SizeUnits import SizeUnit
from src.word_counter.services.commands.size.size_unit_from_str import (
    size_unit_from_str,
)
from src.word_counter.services.options.format.format_type_from_str import (
    format_type_from_str,
)


@click.command
@click.pass_context
@click.argument(
    "files",
    type=click.Path(exists=True, path_type=Path, dir_okay=False, file_okay=True),
    nargs=-1,
)
@click.option(
    "--unit",
    type=click.Choice(SizeUnit.values(), case_sensitive=False),
    default=SizeUnit.BYTES.value,
    show_default=True,
    prompt="Choose a unit for size",
)
@click.option(
    "--ignore-line-sep", is_flag=True, default=False, show_default=True, type=bool
)
def scan(ctx: click.Context, files: list[Path], unit: str, ignore_line_sep: bool):
    output_format = ctx.obj["format"]
    format_type = format_type_from_str(output_format)

    size_unit = size_unit_from_str(unit)

    files_data: list[dict[str, object]] = []

    for file in files:
        files_data.append(
            {
                f"{file.as_posix()}": {
                    "size": filesize(file, size_unit),
                    "words": words_count(file),
                    "lines": lines_count(file),
                    "chars": char_count(file, ignore_line_sep),
                }
            }
        )

    data = output_formatter(files_data, format_type)

    click.echo(data)
