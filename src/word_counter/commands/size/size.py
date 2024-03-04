import click
from pathlib import Path

from src.word_counter.commands.size.SizeUnits import SizeUnit


@click.command
@click.argument(
    "filename", type=click.Path(exists=True, path_type=Path, file_okay=True)
)
@click.option("--unit", type=str, default="B")
def size(filename: Path, unit: str):
    file_size_in_bytes = filename.stat().st_size

    file_size: float = file_size_in_bytes
    
    match unit:
        case SizeUnit.BYTES.value:
            file_size = float(file_size_in_bytes)
        case SizeUnit.KILOBYTES.value:
            file_size = file_size_in_bytes / 1e3
        case SizeUnit.MEGABYTES.value:
            file_size = file_size_in_bytes / 1e6
        case SizeUnit.GIGABYTES.value:
            file_size = file_size_in_bytes / 1e9
        case SizeUnit.TERABYTES.value:
            file_size = file_size_in_bytes / 1e12
        case _:
            raise click.exceptions.BadArgumentUsage("Unrecognized size unit")

    click.echo(f"{filename.name} has {file_size}{unit}")
