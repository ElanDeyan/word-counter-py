import os
from pathlib import Path
from src.word_counter.utils.SizeUnits import SizeUnit


def filesize(
    content: str | Path, output_unit: SizeUnit, decimal_precision: int = 2
) -> str:
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
