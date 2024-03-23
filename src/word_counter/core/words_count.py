from pathlib import Path
from typing import TextIO


def words_count(filepath: Path | TextIO) -> int:
    if isinstance(filepath, Path):
        with open(filepath, "r") as file:
            return len(file.read().split())
    else:
        return len(filepath.read().split())
