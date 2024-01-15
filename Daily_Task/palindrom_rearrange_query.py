from typing import List


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def is_possible(s, query):
            f_h = s[: len(s) // 2]
            s_h = s[len(s) // 2 :][::-1]
