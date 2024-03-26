from typing import List

"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [x for x in nums if x > 0]
        if 1 not in nums:
            return 1
        for num in nums:
            if abs(num) > len(nums):
                continue
            if nums[abs(num) - 1] < 0:
                continue
            nums[abs(num) - 1] *= -1
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return len(nums) + 1


solution = Solution()
print(solution.firstMissingPositive(nums=[1, 2, 0]))
