import os


def char_count(content: str, ignore_line_sep: bool = False) -> int:
    """
    The function `char_count` returns the number of characters in a string, optionally ignoring line
    separators.

    :param content: The `content` parameter is a string that represents the text content for which you
    want to count the characters
    :type content: str
    :param ignore_line_sep: The `ignore_line_sep` parameter is a boolean flag that indicates whether or
    not to ignore line separators when counting characters in the `content` string. If `ignore_line_sep`
    is set to `True`, the function will strip out line separators (such as newline characters) from the
    `content`, defaults to False
    :type ignore_line_sep: bool (optional)
    :return: the length of the input `content` after stripping any line separators if `ignore_line_sep`
    is set to True.
    """
    return len(content.strip(os.linesep) if ignore_line_sep else content)
