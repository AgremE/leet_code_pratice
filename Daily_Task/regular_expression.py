def isMatch(s: str, p: str) -> bool:
    """
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).
    using dynamic alogithm
    """
    # Create a 2D array to store the result
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    # set the first element to be True
    dp[0][0] = True
    # set the first row
    for i in range(1, len(p) + 1):
        if p[i - 1] == "*":
            dp[0][i] = dp[0][i - 2]
    # fill the rest of the table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            else:
                dp[i][j] = False
    return dp[-1][-1]
