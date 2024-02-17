from typing import List
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i_d = 0
        total_sum = 0
        cur_min_len = math.inf
        for i in range(len(nums)):
            total_sum += nums[i]
            while total_sum >= target:
                cur_min_len = min(cur_min_len, i - i_d + 1)
                total_sum -= nums[i_d]
                i_d += 1
        return 0 if cur_min_len == math.inf else cur_min_len


solution = Solution()
print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(solution.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(solution.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
