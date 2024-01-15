from typing import List
import math


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def recurve(nums, i, cur_max, memoir):
            if i >= len(nums):
                return -math.inf
            if i in memoir:
                return memoir[i]
            if nums[i] > cur_max:
                memoir[i] = max(
                    [
                        recurve(nums, i + 1, nums[i], memoir) + 1,
                        recurve(nums, i + 1, cur_max, memoir),
                    ]
                )
            else:
                memoir[i] = max(recurve(nums, i + 1, cur_max, memoir), 1)
            return memoir[i]

        memoir = {}
        result = recurve(nums, 0, -(10**5), memoir)
        return result


solution = Solution()
# print(solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
print(solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
# print(solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
