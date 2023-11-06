from typing import List
import sys


class Solution:
    def findMaxSubarry(self, nums: List[int], restrict_len: int) -> int:
        _max = -(10**5)
        f_index = 0
        s_index = 0
        total_sum = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if f_index > len_nums - 1 or s_index > len_nums - 1:
                break
            total_sum = total_sum + nums[f_index]
            if (total_sum < 0) or (f_index - s_index == restrict_len - 1):
                curr_move_s_index = 0
                for j in range(f_index - s_index):
                    curr_move_s_index = j + 1
                    total_sum = total_sum - nums[s_index + j]
                    if total_sum > 0:
                        break
                s_index = s_index + curr_move_s_index
            if total_sum >= _max:
                _max = total_sum
            if total_sum >= 0:
                f_index = f_index + 1
            else:
                total_sum = 0
                for x in range(f_index, len_nums):
                    f_index = x
                    s_index = x
                    if nums[x] >= _max:
                        _max = nums[x]
                    if nums[x] >= 0:
                        break
        return _max

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        max_ending_at = 0
        min_ending_at = 0
        max_sum = -sys.maxsize - 1
        min_sum = sys.maxsize

        for x in nums:
            total_sum += x
            max_ending_at = max(max_ending_at + x, x)
            max_sum = max(max_ending_at, max_sum)
            min_ending_at = min(min_ending_at + x, x)
            min_sum = min(min_ending_at, min_sum)

        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        return max_sum


solution = Solution()
print(solution.maxSubarraySumCircular([-1, -2, 5]))
