from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # Just counting elem in array algo would work
        # each elem of array is num tiering and non_tiering day
        # take the max len of sub array that have the highest positive different
        s_i, f_i = 0, 0
