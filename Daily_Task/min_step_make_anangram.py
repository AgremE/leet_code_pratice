from typing import List
import math


class Solution:
    def jump(self, nums: List[int]) -> int:
        def find_swap_inx(nums):
            swap_indx = len(nums) - 1
            while swap_indx != 0:
                if nums[swap_indx] <= nums[swap_indx - 1]:
                    swap_indx -= 1
                    continue
                break
            swap_indx -= 1
            next_p = -1
            _max = math.inf
            for i in range(swap_indx, len(nums)):
                if nums[swap_indx] < nums[i] and _max >= nums[i]:
                    next_p = i
                    _max = nums[i]
            return swap_indx, next_p

        def swap(nums, i, j):
            _temp = nums[j]
            nums[j] = nums[i]
            nums[i] = _temp

        swap_indx, next_p = find_swap_inx(nums)
        swap(nums, swap_indx, next_p)
        nums[swap_indx + 1 :] = sorted(nums[swap_indx + 1 :])
        return nums


solution = Solution()
print(solution.jump(nums=[2, 3, 1]))
print(solution.jump(nums=[1, 3, 2]))
print(solution.jump(nums=[3, 2, 1]))
print(solution.jump(nums=[1, 1, 5]))
