import click
from pathlib import Path

from src.word_counter.commands.size.SizeUnits import SizeUnit
from src.word_counter.services.commands.size.file_and_size import FileData
from src.word_counter.services.commands.size.size_from_bytes import size_from_bytes
from src.word_counter.services.commands.size.size_unit_from_str import (
    size_unit_from_str,
)
from src.word_counter.services.options.format.format_type_from_str import (
    format_type_from_str,
)
from src.word_counter.services.options.format.output_formatter import output_formatter


unit_help_message = "Size unit (written in UPPERCASE)."


@click.command
@click.pass_context
@click.argument(
    "files",
    type=click.Path(exists=True, path_type=Path, dir_okay=False, file_okay=True),
    nargs=-1,
)
@click.option(
    "--unit",
    type=click.Choice(SizeUnit.values()),
    default=SizeUnit.BYTES.value,
    show_default=True,
    help=unit_help_message,
)
def size(ctx: click.Context, files: list[Path], unit: str):
    output_format: str = ctx.obj["format"]
    format_type = format_type_from_str(output_format)

    size_unit = size_unit_from_str(unit)

    files_and_sizes: list[dict[str, object]] = []

    for filepath in files:
        file_size = size_from_bytes(filepath.stat().st_size, output_unit=size_unit)
        files_and_sizes.append(
            dict(FileData(filepath=filepath.as_posix(), size=file_size, unit=size_unit.value))
        )

    data = output_formatter(files_and_sizes, format_type)

    click.echo(data)
