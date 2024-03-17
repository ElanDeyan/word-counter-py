import os
from pathlib import Path


def char_count(filepath: Path, ignore_line_sep: bool = False) -> int:
    with open(filepath, "r") as file:
        content = file.read().strip(os.linesep) if ignore_line_sep else file.read()

        return len(content)
