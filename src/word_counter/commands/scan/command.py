from pathlib import Path
import click

from src.word_counter.commands.common_options import common_options
from src.word_counter.core.char_count import char_count
from src.word_counter.core.filesize import filesize
from src.word_counter.core.lines_count import lines_count
from src.word_counter.core.words_count import words_count
from src.word_counter.docs.options.ignore_line_sep_help import IGNORE_LINE_SEP_HELP
from src.word_counter.docs.options.unit_help import UNIT_HELP
from src.word_counter.services.options.format.output_formatter import output_formatter
from src.word_counter.utils.SizeUnits import SizeUnit
from src.word_counter.services.commands.size.size_unit_from_str import (
    size_unit_from_str,
)
from src.word_counter.services.options.format.format_type_from_str import (
    format_type_from_str,
)


@click.command
@click.pass_context
@click.argument(
    "files",
    type=click.Path(exists=True, path_type=Path, dir_okay=False, file_okay=True),
    nargs=-1,
)
@common_options
@click.option(
    "--unit",
    type=click.Choice(SizeUnit.values(), case_sensitive=False),
    default=SizeUnit.BYTES.value,
    show_default=True,
    help=UNIT_HELP,
)
@click.option(
    "--ignore-line-sep",
    is_flag=True,
    default=False,
    show_default=True,
    type=bool,
    help=IGNORE_LINE_SEP_HELP,
)
def scan(
    ctx: click.Context,
    files: list[Path],
    output_format: str,
    unit: str,
    ignore_line_sep: bool,
):
    """
    Scans FILES content for size, words, lines, and characters, and outputs the data in a specified format.
    """
    format_type = format_type_from_str(output_format)

    size_unit = size_unit_from_str(unit)

    files_data: list[dict[str, object]] = []

    if ctx.obj["stdin"] is not None:
        stdin_output: str = ctx.obj["stdin"].read()

        files_data.append(
            {
                "stdin": {
                    "size": filesize(stdin_output, size_unit),
                    "words": words_count(stdin_output),
                    "lines": lines_count(stdin_output),
                    "chars": char_count(stdin_output, ignore_line_sep),
                }
            }
        )

    for file in files:
        with open(file) as f:
            file_content = f.read()
            files_data.append(
                {
                    f"{file.as_posix()}": {
                        "size": filesize(file_content, size_unit),
                        "words": words_count(file_content),
                        "lines": lines_count(file_content),
                        "chars": char_count(file_content, ignore_line_sep),
                    }
                }
            )

    data = output_formatter(files_data, format_type)

    click.echo(data)
