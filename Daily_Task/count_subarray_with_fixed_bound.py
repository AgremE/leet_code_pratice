from typing import List
import math


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        max_i, min_i = math.inf, math.inf
        most_v_i = 0
        result = 0
        for i, num in enumerate(nums):
            if num == minK:
                min_i = i
            elif num == maxK:
                max_i = i
            elif (num < minK) and (num > maxK):
                most_v_i = i
            if max_i == math.inf or min_i == math.inf:
                continue
            result += max(0, i - ((min(min_i, max_i) - most_v_i)))
        return result


solution = Solution()
print(solution.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
