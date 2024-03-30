import click
from pathlib import Path

from src.word_counter.commands.common_options import common_options
from src.word_counter.core.filesize import filesize
from src.word_counter.docs.options.decimal_precision_help import DECIMAL_PRECISION_HELP
from src.word_counter.docs.options.unit_help import UNIT_HELP
from src.word_counter.utils.SizeUnits import SizeUnit
from src.word_counter.services.commands.size.size_unit_from_str import (
    size_unit_from_str,
)
from src.word_counter.services.options.format.format_type_from_str import (
    format_type_from_str,
)
from src.word_counter.services.options.format.output_formatter import output_formatter


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
    type=click.Choice(SizeUnit.short_names(), case_sensitive=False),
    default=SizeUnit.BYTES.value.short_name,
    show_default=True,
    help=UNIT_HELP,
)
@click.option(
    "--decimal-precision",
    type=click.INT,
    default=2,
    show_default=True,
    help=DECIMAL_PRECISION_HELP,
)
def size(
    ctx: click.Context,
    files: list[Path],
    output_format: str,
    unit: str,
    decimal_precision: int,
):
    """
    Calculates the sizes of the FILES, and outputs the data in the specified format.
    """
    format_type = format_type_from_str(output_format)

    size_unit = size_unit_from_str(unit)

    files_and_sizes: list[dict[str, object]] = []

    if ctx.obj["stdin"] is not None:
        stdin_output: str = ctx.obj["stdin"].read()

        files_and_sizes.append(
            {
                "filepath": "stdin",
                "size": filesize(stdin_output, size_unit, decimal_precision),
            }
        )

    for filepath in files:
        files_and_sizes.append(
            {
                "filepath": filepath.as_posix(),
                "size": filesize(filepath, size_unit, decimal_precision),
            }
        )

    data = output_formatter(files_and_sizes, format_type)

    click.echo(data)
