from typing import List
import math


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        f_i, s_i = 0, 0
        tracker = {}
        _max = -math.inf
        while f_i != len(nums):
            next_c = nums[f_i]
            if next_c in tracker:
                tracker[next_c] += 1
            else:
                tracker[next_c] = 1
            if tracker[next_c] > k:
                while True:
                    tracker[nums[s_i]] -= 1
                    s_i += 1
                    if tracker[nums[s_i]] == 0:
                        del tracker[nums[s_i]]
                    if tracker[next_c] <= k:
                        break
            _max = max(_max, (f_i - s_i + 1))
            f_i += 1
        return _max


solution = Solution()
print(solution.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
