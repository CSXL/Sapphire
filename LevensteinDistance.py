# find a module(cython) to do it
def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Computesz the Levenshtein distance between two strings.

    Args:
    ----
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    -------
    int: The Levenshtein distance between the two strings.
    """

    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the first row and column with consecutive integers
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    # Return the final value in the DP table
    return dp[m][n]
