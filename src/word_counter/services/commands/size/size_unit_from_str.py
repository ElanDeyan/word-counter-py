import click
from src.word_counter.utils.SizeUnits import SizeUnit


def size_unit_from_str(string: str) -> SizeUnit:
    """
    The function `size_unit_from_str` converts a string representation of a size unit to the
    corresponding `SizeUnit` enum value.

    :param string: The `size_unit_from_str` function takes a string input and converts it into a
    `SizeUnit` enum value based on the short name of the enum values. The function handles conversion
    for size units like Bytes, Kilobytes, Megabytes, Gigabytes, and Terabytes
    :type string: str
    """
    try:
        match string.upper():
            case SizeUnit.BYTES.value.short_name:
                return SizeUnit.BYTES
            case SizeUnit.KILOBYTES.value.short_name:
                return SizeUnit.KILOBYTES
            case SizeUnit.MEGABYTES.value.short_name:
                return SizeUnit.MEGABYTES
            case SizeUnit.GIGABYTES.value.short_name:
                return SizeUnit.GIGABYTES
            case SizeUnit.TERABYTES.value.short_name:
                return SizeUnit.TERABYTES
            case _:
                raise ValueError()
    except ValueError:
        raise click.exceptions.BadParameter(f"Unrecognized size unit: {string}.")
