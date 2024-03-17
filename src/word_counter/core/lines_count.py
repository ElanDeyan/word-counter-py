from pathlib import Path


def lines_count(filepath: Path) -> int:
    with open(filepath, "r") as file:
        return len(file.readlines())
