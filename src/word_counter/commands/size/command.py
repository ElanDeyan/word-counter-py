import json
import click
from pathlib import Path

from src.word_counter.commands.size.SizeUnits import SizeUnit
from src.word_counter.helpers.size.file_and_size import FileData
from src.word_counter.helpers.size.size_from_bytes import size_from_bytes
from src.word_counter.helpers.size.size_unit_from_str import size_unit_from_str


unit_help_message = "Size unit (written in UPPERCASE)."


@click.command
@click.argument(
    "files",
    type=click.Path(exists=True, path_type=Path, file_okay=True),
    nargs=-1,
)
@click.option(
    "--unit",
    type=click.Choice(SizeUnit.values()),
    default=SizeUnit.BYTES.value,
    show_default=True,
    help=unit_help_message,
)
def size(files: list[Path], unit: str):
    size_unit = size_unit_from_str(unit)

    files_and_sizes: list[FileData] = []

    for file in files:
        file_size = size_from_bytes(file.stat().st_size, output_unit=size_unit)
        files_and_sizes.append(
            FileData(file=file.name, size=file_size, unit=size_unit.value)
        )

    json_data = json.dumps(files_and_sizes)

    click.echo(json_data)
