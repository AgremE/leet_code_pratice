from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        len_n = len(nums)
        upper_bound = len_n - 1
        lower_bound = 0
        left_ind = -1
        right_ind = -1
        ### Finding the left index
        while lower_bound <= upper_bound:
            mid_ind = (lower_bound + upper_bound) // 2
            ind_num = nums[mid_ind]
            if target == ind_num:
                left_ind = mid_ind
                upper_bound = mid_ind - 1
                mid_ind = (lower_bound + upper_bound) // 2
            elif ind_num < target:
                lower_bound = mid_ind + 1
                mid_ind = (lower_bound + upper_bound) // 2
            elif ind_num > target:
                upper_bound = mid_ind - 1
                mid_ind = (lower_bound + upper_bound) // 2
        ### Finding the right index
        upper_bound = len_n - 1
        lower_bound = 0
        while lower_bound <= upper_bound:
            mid_ind = (lower_bound + upper_bound) // 2
            ind_num = nums[mid_ind]
            if target == ind_num:
                right_ind = mid_ind
                lower_bound = mid_ind + 1
                mid_ind = (lower_bound + upper_bound) // 2
            elif ind_num < target:
                lower_bound = mid_ind + 1
                mid_ind = (lower_bound + upper_bound) // 2
            elif ind_num > target:
                upper_bound = mid_ind - 1
                mid_ind = (lower_bound + upper_bound) // 2
        return [left_ind, right_ind]


test_case_1 = [5, 7, 7, 8, 8, 10]  # 8
test_case_2 = [5, 7, 7, 8, 8, 10]  # 6
test_case_3 = [5, 7, 7, 8, 8, 10]  # 2

test_solution = Solution()
print(test_solution.searchRange(test_case_1, 5))
print(test_solution.searchRange(test_case_2, 8))
print(test_solution.searchRange(test_case_2, 7))
print(test_solution.searchRange(test_case_3, 2))
