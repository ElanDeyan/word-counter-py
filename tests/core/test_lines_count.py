from pathlib import Path

from src.word_counter.core.lines_count import lines_count


def test_lines_count(test_files: list[Path]):
    for test_file in test_files:
        with open(test_file, 'r', encoding="utf-8") as f:
            assert len(f.readlines()) == lines_count(f.read())