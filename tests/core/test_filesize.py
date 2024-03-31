import os
from pathlib import Path
import pytest

from src.word_counter.core.filesize import filesize
from src.word_counter.utils.SizeUnits import SizeUnit
from tests.conftest import convert_size


@pytest.fixture
def test_files_size_in_bytes(test_files: list[Path]) -> list[int]:
    return [os.path.getsize(test_file) for test_file in test_files]


@pytest.fixture
def size_units_values():
    return SizeUnit._member_map_.values()


def test_size_in_bytes(test_files_size_in_bytes: list[int], test_files: list[Path]):
    for test_file, test_file_size_in_bytes in zip(test_files, test_files_size_in_bytes):
        expected_output = f"{test_file_size_in_bytes}B"
        assert filesize(test_file, SizeUnit.BYTES) == expected_output


def test_size_all_units(
    test_files: list[Path],
    test_files_size_in_bytes: list[int],
    size_units_values: list[SizeUnit],
):
    for size_unit in size_units_values:
        for test_file, test_file_size_in_bytes in zip(
            test_files, test_files_size_in_bytes
        ):
            converted_size = convert_size(test_file_size_in_bytes, size_unit)
            expected_output = f"{converted_size}{size_unit.value.short_name}"
            assert filesize(test_file, size_unit) == expected_output
