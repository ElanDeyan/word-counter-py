import click
from src.word_counter.commands.size.SizeUnits import SizeUnit


def size_unit_from_str(string: str) -> SizeUnit:
    """
    The function `size_unit_from_str` converts a string to a SizeUnit enum, raising an exception for
    unrecognized size units.

    :param string: The `string` parameter is a string value that represents a size unit. The function
    `size_unit_from_str` attempts to convert this string into a `SizeUnit` enum value. If the string is
    not recognized as a valid size unit, it raises a `click.exceptions.BadParameter` exception with
    :type string: str
    :return: The `size_unit_from_str` function is returning a `SizeUnit` object based on the input
    string. If the input string is already in uppercase, it returns a `SizeUnit` object with that
    string. If the input string is not in uppercase, it converts it to uppercase before creating the
    `SizeUnit` object. If the input string is not a valid size unit, it raises a
    :raise: `click.exceptions.BadParameter`.
    """
    try:
        return SizeUnit(string)
    except ValueError:
        raise click.exceptions.BadParameter(f"Unrecognized size unit: {string}.")
