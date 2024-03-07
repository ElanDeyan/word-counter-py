from pathlib import Path
import pytest
from click.testing import CliRunner
from src.word_counter.main import cli

EXAMPLE_DIRECTORY = "src/data/"
EXAMPLE_FILE_NAME = "example.txt"


@pytest.fixture
def example_size_in_bytes():
    return Path(EXAMPLE_DIRECTORY + EXAMPLE_FILE_NAME).stat().st_size


def test_size(example_size_in_bytes: int):
    runner = CliRunner()
    result = runner.invoke(cli, ["size", "--unit", "B", EXAMPLE_DIRECTORY])
    assert result.exit_code == 0
    assert f"{{filename: {EXAMPLE_FILE_NAME}, size: {float(example_size_in_bytes)}, unit: B}}"
