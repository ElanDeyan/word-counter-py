from pathlib import Path


def words_count(filepath: Path) -> int:
    with open(filepath, "r") as file:
        return len(file.read().split())
