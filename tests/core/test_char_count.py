import os
from pathlib import Path

import pytest

from src.word_counter.core.char_count import char_count

@pytest.fixture
def ignore_line_sep():
    return False

@pytest.fixture
def test_files_char_count(test_files: list[Path], ignore_line_sep: bool):
    files_char_count: list[int] = []
    for test_file in test_files:
        with open(test_file, "r") as f:
            content = f.read()

            files_char_count.append(
                len(content.strip(os.linesep) if ignore_line_sep else content.strip())
            )

    return files_char_count


def test_char_count(test_files: list[Path], test_files_char_count: list[int], ignore_line_sep: bool):
    files_char_count: list[int] = []
    for test_file in test_files:
        with open(test_file, 'r', encoding="utf-8") as f:
            content = f.read()
            files_char_count.append(char_count(content, ignore_line_sep))

    assert files_char_count == test_files_char_count
