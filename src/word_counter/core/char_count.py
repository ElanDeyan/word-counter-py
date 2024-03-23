import os


def char_count(content: str, ignore_line_sep: bool = False) -> int:
    return len(content.strip(os.linesep) if ignore_line_sep else content)
