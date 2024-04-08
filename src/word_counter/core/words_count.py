def words_count(content: str) -> int:
    """
    The function `words_count` takes a string as input and returns the number of words in the string by
    splitting it based on whitespace.

    :param content: A string containing words that you want to count
    :type content: str
    :return: The function `words_count` returns the number of words in the input `content` string.
    """
    return len(content.split())
