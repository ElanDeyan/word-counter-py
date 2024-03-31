from pathlib import Path
import pytest
from src.word_counter.utils.SizeUnits import SizeUnit


@pytest.fixture
def test_data_directory():
    return "./data"


@pytest.fixture
def test_files(test_data_directory: str) -> list[Path]:
    dir_path = Path(test_data_directory)

    files = list(dir_path.glob("*"))

    files = [Path(file) for file in files if file.is_file()]

    return files


def convert_size(
    size_in_bytes: int, target_unit: SizeUnit, decimal_precision: int = 2
) -> float:
    """
    The function `convert_size` converts a size in bytes to a specified unit with a specified decimal
    precision.

    :param size_in_bytes: The `size_in_bytes` parameter represents the size in bytes that you want to
    convert to a different unit of size
    :type size_in_bytes: int
    :param target_unit: The `target_unit` parameter in the `convert_size` function is of type
    `SizeUnit`. It is used to specify the unit to which the size in bytes should be converted. The
    `SizeUnit` is likely an enumeration or a custom class that defines different units such as bytes,
    kiloby
    :type target_unit: SizeUnit
    :param decimal_precision: The `decimal_precision` parameter in the `convert_size` function specifies
    the number of decimal places to round the converted size to. This parameter determines the level of
    precision in the output of the size conversion
    :type decimal_precision: int
    :return: the size in the specified target unit with the specified decimal precision.
    """
    return round(
        size_in_bytes / (target_unit.value.conversion_from_bytes_factor),
        decimal_precision,
    )
