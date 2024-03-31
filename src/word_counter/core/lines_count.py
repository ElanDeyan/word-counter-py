def lines_count(content: str) -> int:
    """
    The function `lines_count` takes a string as input and returns the number of lines in the string.
    
    :param content: A string containing text content
    :type content: str
    :return: The function `lines_count` returns the number of lines in the input `content` string. It
    achieves this by splitting the string into lines using the `splitlines()` method and then returning
    the length of the resulting list of lines.
    """
    return len(content.splitlines())
