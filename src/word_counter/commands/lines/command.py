from pathlib import Path
import click


@click.command
@click.argument(
    "filepath", type=click.Path(exists=True, path_type=Path, file_okay=True)
)
def lines(filepath: Path):
    """
    Prints the number of lines present in the file.
    """
    with open(filepath.name, "r") as file:
        click.echo(f"{{filename: {filepath.name}, lines: {len(file.readlines())}}}")
