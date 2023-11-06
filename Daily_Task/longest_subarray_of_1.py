from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Just try to delete the zero that make the most potential impact on one count
        Definition of most potential impact of counting one:
        The single zero, zero that connect two 1
        if no such zero exist, does not matter, which way you delete, you will have
        the same longest one
        if no such zero exist, you can delete any if first observerbal zero
        if zero present, just delete first number one, it should also work
        """
        pass
