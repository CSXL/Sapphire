import Levenshtein


def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Calculates the Levenshtein distance between two input strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    return Levenshtein.distance(str1, str2)
