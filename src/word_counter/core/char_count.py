import os
from pathlib import Path
from typing import TextIO


def char_count(filepath: Path | TextIO, ignore_line_sep: bool = False) -> int:
    content: str

    if isinstance(filepath, Path):
        with open(filepath, "r") as file:
            content = file.read().strip(os.linesep) if ignore_line_sep else file.read()
    else:
        content = (
            filepath.read().strip(os.linesep) if ignore_line_sep else filepath.read()
        )

    return len(content)
