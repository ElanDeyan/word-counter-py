import click

from src.word_counter.commands.lines.command import lines
from src.word_counter.commands.size.command import size
from src.word_counter.options.format.OutputFormats import OutputFormats

from src.word_counter.commands.words.command import words


@click.group
@click.option(
    "--format",
    "output_format",
    type=click.Choice(OutputFormats.values(), case_sensitive=False),
    default=OutputFormats.PLAINTEXT.value,
    show_default=True,
    prompt="Choose a format"
)
def cli(output_format: str):
    click.get_current_context().obj = {"format": output_format}


cli.add_command(size)
cli.add_command(lines)
cli.add_command(words)


if __name__ == "__main__":
    cli()
