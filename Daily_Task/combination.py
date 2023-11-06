from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Moving constructive list backward
        list_nums = [[x for x in range(1, n + 1)] for y in range(k)]
        result = []
        for i in range(list_nums):
