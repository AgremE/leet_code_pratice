from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        track_number_zero = 0
        zero_index = None
        total_prod = 1
        result = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                total_prod = total_prod * num
            else:
                track_number_zero = track_number_zero + 1
                zero_index = i
        if track_number_zero > 1:
            return [0 for x in range(len(nums))]
        elif track_number_zero == 1:
            result[zero_index] = total_prod
        else:
            result = [int(total_prod / nums[i]) for i in range(len(nums))]
        return result


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
