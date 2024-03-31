from pathlib import Path

from src.word_counter.core.words_count import words_count


def test_words_count(test_files: list[Path]):
    for test_file in test_files:
        with open(test_file, 'r', encoding="utf-8") as f:
            assert len(f.read().split()) == words_count(f.read())