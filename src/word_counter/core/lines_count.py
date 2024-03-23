from pathlib import Path
from typing import TextIO


def lines_count(filepath: Path | TextIO) -> int:
    if isinstance(filepath, Path):
        with open(filepath, "r") as file:
            return len(file.readlines())
    else:
        return len(filepath.readlines())
