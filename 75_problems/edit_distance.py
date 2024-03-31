"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

import math


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Just use DP
        """

        def recurve(word1, word2, i1, i2, memoir):
            pass
