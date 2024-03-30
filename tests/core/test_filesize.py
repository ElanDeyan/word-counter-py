import os
from pathlib import Path
import pytest

from src.word_counter.core.filesize import filesize
from src.word_counter.utils.SizeUnits import SizeUnit
from tests.conftest import convert_size
from tests.constants import EXAMPLE_DIRECTORY, TEST_FILE_NAME


@pytest.fixture
def test_file():
    return Path(EXAMPLE_DIRECTORY + TEST_FILE_NAME)


@pytest.fixture
def test_file_size_in_bytes(test_file: Path):
    return os.path.getsize(test_file)


@pytest.fixture
def size_units_values():
    return SizeUnit._member_map_.values()


def test_size_in_bytes(test_file_size_in_bytes: int, test_file: Path):
    assert f"{test_file_size_in_bytes}" in filesize(test_file, SizeUnit.BYTES)


def test_size_all_units(
    test_file: Path, test_file_size_in_bytes: int, size_units_values: list[SizeUnit]
):
    for size_unit in size_units_values:
        converted_size = convert_size(test_file_size_in_bytes, size_unit)

        assert f"{converted_size}" in filesize(test_file, size_unit)
