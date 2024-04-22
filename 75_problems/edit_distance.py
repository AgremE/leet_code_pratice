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
        if len(word2)==0 or len(word1)==0:
            return max(len(word1),len(word2))

        def recurve(word1, word2, i1,i2, memoir):
            mins_one = 1 
            if i1== len(word1):
                return max(0,len(word2)-i2)
            if i2 == len(word2):
                return max(0,len(word1)-i1)
            if memoir[i1][i2]!=math.inf:
                return memoir[i1][i2]
            
            if word1[i1]==word2[i2]:
                memoir[i1][i2] = recurve(word1, word2, i1+1,i2+1, memoir)
            else:
                memoir[i1][i2] = min(
                    [
                        recurve(word1, word2, i1+1,i2, memoir)+1, # delete
                        recurve(word1, word2, i1+1,i2+1, memoir)+1, # replace
                        recurve(word1, word2, i1,i2+1, memoir)+1, # insert
                    ]
                )
            return memoir[i1][i2]
        memoir = [[math.inf for _ in range(len(word2))] for _ in range(len(word1))]
        result = recurve(word1, word2, 0,0, memoir)
        return result
    
solution = Solution()
# print(solution.minDistance( word1 = "aa", word2 = "aa"))
# print(solution.minDistance( word1 = "test", word2 = "testttt"))
# print(solution.minDistance(word1 = "intention", word2 = "execution"))
print(solution.minDistance( word1 = "horse", word2 = "ros"))