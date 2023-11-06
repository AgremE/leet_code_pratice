from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp = []
        for i in range(len(nums)):
            temp.append([nums[i]])
