import os
from pathlib import Path
import pytest

from src.word_counter.core.filesize import filesize
from src.word_counter.utils.SizeUnits import SizeUnit
from tests.constants import EXAMPLE_DIRECTORY, TEST_FILE_NAME


@pytest.fixture
def test_file():
    return Path(EXAMPLE_DIRECTORY + TEST_FILE_NAME)


@pytest.fixture
def test_file_size_in_bytes(test_file: Path):
    return os.path.getsize(test_file)


def test_size_in_bytes(test_file_size_in_bytes: int, test_file: Path):
    assert f"{test_file_size_in_bytes}" in filesize(test_file, SizeUnit.BYTES)
