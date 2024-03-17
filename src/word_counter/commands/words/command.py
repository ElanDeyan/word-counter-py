from pathlib import Path
import click

from src.word_counter.core.words_count import words_count
from src.word_counter.services.options.format.format_type_from_str import (
    format_type_from_str,
)
from src.word_counter.services.options.format.output_formatter import output_formatter


@click.command
@click.pass_context
@click.argument(
    "files", type=click.Path(exists=True, path_type=Path, file_okay=True), nargs=-1
)
def words(ctx: click.Context, files: list[Path]):
    output_format: str = ctx.obj["format"]
    format_type = format_type_from_str(output_format)
    files_and_words: list[dict[str, object]] = []

    for filepath in files:
        files_and_words.append({
            "filepath": filepath.as_posix(),
             "words_count": words_count(filepath)
            }
        )

    data = output_formatter(files_and_words, format_type)

    click.echo(data)
