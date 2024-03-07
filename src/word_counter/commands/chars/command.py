import os
from pathlib import Path
import click


@click.command
@click.argument(
    "filepath", type=click.Path(exists=True, path_type=Path, file_okay=True)
)
@click.option(
    "--ignore-line-sep", is_flag=True, default=False, show_default=True, type=bool
)
def chars(filepath: Path, ignore_line_sep: bool):
    with open(filepath.name, "r", encoding="utf-8") as file:
        content = file.read().strip(os.linesep) if ignore_line_sep else file.read()
        click.echo(f"{{filename: {filepath.name}, chars: {len(content)}}}")
