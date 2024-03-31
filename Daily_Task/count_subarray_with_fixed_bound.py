from typing import List
import math


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        s_i, f_i = 0, 0
        min_ind = []
        max_ind = []
        result = 0
        while f_i < len(nums):
            if nums[f_i] == minK:
                min_ind.append(f_i)
                if max_ind or (f_i == len(nums) - 1):
                    for _i, ind in enumerate(max_ind):
                        if _i == 0:
                            result += ind - s_i
                        else:
                            result += max_ind[ind] - max_ind[ind - 1]
                f_i += 1
            elif nums[f_i] == maxK:
                max_ind.append(f_i)
                if min_ind or (f_i == len(nums) - 1):
                    for _i, ind in enumerate(min_ind):
                        if _i == 0:
                            result += ind - s_i
                        else:
                            result += min_ind[ind] - min_ind[ind - 1]
                f_i += 1
            elif nums[f_i] < minK or nums[f_i] > maxK:
                f_i += 1
                s_i = f_i
                min_ind = []
                max_ind = []
            else:
                f_i += 1
        return result


solution = Solution()
print(solution.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
