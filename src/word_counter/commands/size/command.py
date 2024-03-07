import click
from pathlib import Path

from src.word_counter.commands.size.OutputFormats import OutputFormats
from src.word_counter.commands.size.SizeUnits import SizeUnit
from src.word_counter.services.size.file_and_size import FileData
from src.word_counter.services.size.format_type_from_str import format_type_from_str
from src.word_counter.services.size.output_formatter import output_formatter
from src.word_counter.services.size.size_from_bytes import size_from_bytes
from src.word_counter.services.size.size_unit_from_str import size_unit_from_str


unit_help_message = "Size unit (written in UPPERCASE)."


@click.command
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
@click.option(
    "--format","output_format",
    type=click.Choice(OutputFormats.values()),
    default=OutputFormats.PLAINTEXT.value,
    show_default=True,
)
def size(files: list[Path], unit: str, output_format: str):
    size_unit = size_unit_from_str(unit)
    format_type = format_type_from_str(output_format)

    files_and_sizes: list[FileData] = []

    for file in files:
        file_size = size_from_bytes(file.stat().st_size, output_unit=size_unit)
        files_and_sizes.append(
            FileData(file=file.name, size=file_size, unit=size_unit.value)
        )

    data = output_formatter(files_and_sizes, format_type)

    click.echo(data)
