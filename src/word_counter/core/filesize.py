import os
from pathlib import Path
from src.word_counter.utils.SizeUnits import SizeUnit


def filesize(
    content: str | Path, output_unit: SizeUnit, decimal_precision: int = 2
) -> str:
    """
    The `filesize` function calculates the size of a file or content in different units and returns the
    size formatted with the specified precision.

    :param content: The `content` parameter in the `filesize` function can be either a string or a
    `Path` object representing the file for which you want to determine the size
    :type content: str | Path
    :param output_unit: The `output_unit` parameter in the `filesize` function is used to specify the
    unit in which the file size should be displayed. It is of type `SizeUnit`, which is an enum or a
    similar data structure that contains different size units like Bytes, Kilobytes, Megabytes, etc
    :type output_unit: SizeUnit
    :param decimal_precision: The `decimal_precision` parameter in the `filesize` function determines
    the number of decimal places to include in the output when converting the file size to a different
    unit. It specifies the level of precision for the converted file size. By default, it is set to 2,
    meaning that the converted file, defaults to 2
    :type decimal_precision: int (optional)
    :return: The `filesize` function returns a formatted string representing the size of the content in
    the specified `output_unit`. The size is calculated based on the content provided, either as a
    string or a file path. The size is converted to the desired `output_unit` with the specified
    `decimal_precision`. The final result is a string indicating the size with the appropriate unit and
    precision.
    """
    size_in_bytes: int
    if isinstance(content, str):
        try:
            size_in_bytes = len(content.encode(encoding="utf-8"))
        except UnicodeEncodeError as err:
            raise Exception(err.reason)
    else:
        size_in_bytes = os.path.getsize(content)

    if output_unit is SizeUnit.BYTES:
        return f"{float(size_in_bytes)}B"

    return f"{round(size_in_bytes / output_unit.value.conversion_from_bytes_factor, decimal_precision)}{output_unit.value.short_name}"
