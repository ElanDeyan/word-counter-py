import click
from pathlib import Path

from src.word_counter.commands.size.SizeUnits import SizeUnit
from src.word_counter.helpers.size_unit_from_str import size_unit_from_str


@click.command
@click.argument(
    "filename", type=click.Path(exists=True, path_type=Path, file_okay=True)
)
@click.option("--unit", type=str, default="B")
def size(filename: Path, unit: str):
    file_size_in_bytes = filename.stat().st_size

    file_size: float = file_size_in_bytes

    unit_type = size_unit_from_str(unit)

    match unit_type:
        case SizeUnit.BYTES:
            file_size = float(file_size_in_bytes)
        case SizeUnit.KILOBYTES:
            file_size = file_size_in_bytes / 1e3
        case SizeUnit.MEGABYTES:
            file_size = file_size_in_bytes / 1e6
        case SizeUnit.GIGABYTES:
            file_size = file_size_in_bytes / 1e9
        case SizeUnit.TERABYTES:
            file_size = file_size_in_bytes / 1e12

    click.echo(f"{filename.name} has {file_size}{unit}")
