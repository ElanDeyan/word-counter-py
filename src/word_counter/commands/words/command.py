from pathlib import Path
import click


@click.command
@click.argument(
    "filepath", type=click.Path(exists=True, path_type=Path, file_okay=True)
)
def words(filepath: Path):
    with open(filepath, "r") as file:
        words = file.read().split()
        click.echo(f"{{filename: {filepath.name}, words: {len(words)}}}")
