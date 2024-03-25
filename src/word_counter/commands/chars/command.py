from pathlib import Path
import click

from src.word_counter.commands.common_options import common_options
from src.word_counter.core.char_count import char_count
from src.word_counter.docs.options.ignore_line_sep_help import IGNORE_LINE_SEP_HELP
from src.word_counter.services.options.format.format_type_from_str import (
    format_type_from_str,
)
from src.word_counter.services.options.format.output_formatter import output_formatter


@click.command
@click.pass_context
@click.argument(
    "files",
    type=click.Path(exists=True, path_type=Path, file_okay=True),
    nargs=-1,
)
@common_options
@click.option(
    "--ignore-line-sep",
    is_flag=True,
    default=False,
    show_default=True,
    type=bool,
    help=IGNORE_LINE_SEP_HELP,
)
def chars(
    ctx: click.Context, files: list[Path], output_format: str, ignore_line_sep: bool
):
    """
    Counts the characters in each file of FILES, and outputs the results in a specified format.
    """
    format_type = format_type_from_str(output_format)

    files_and_chars: list[dict[str, object]] = []

    if ctx.obj["stdin"] is not None:
        stdin_output: str = ctx.obj["stdin"].read()

        files_and_chars.append({"filepath": "stdin", "chars": char_count(stdin_output)})

    for filepath in files:
        with open(filepath, "r") as f:
            file_content = f.read()
            files_and_chars.append(
                {
                    "filepath": filepath.as_posix(),
                    "chars": char_count(file_content, ignore_line_sep),
                }
            )

    data = output_formatter(files_and_chars, format_type)

    click.echo(data)
