from pathlib import Path
import pytest
from click.testing import CliRunner
from src.word_counter.main import cli

EXAMPLE_DIRECTORY = "src/data/example.txt"
EXAMPLE_FILE_NAME = "example.txt"


@pytest.fixture
def example_size_in_bytes():
    return Path(EXAMPLE_DIRECTORY).stat().st_size

def test_size(example_size_in_bytes: int):
    runner = CliRunner()
    result = runner.invoke(cli, ["size", EXAMPLE_DIRECTORY, "--unit", "B"])
    assert result.exit_code == 0
    assert f"{EXAMPLE_FILE_NAME} has {float(example_size_in_bytes)}B" in result.output
