from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Algorithm
        # Double index because the list already sort in non-decressing
        # One index keep track of change to make list unique
        # Other move to find the unique number
        # #
        f_index = 0
        for i in range(1, len(nums)):
            s_index = i
            f_val = nums[f_index]
            s_val = nums[s_index]
            if f_val == s_val:
                continue
            else:
                f_index = f_index + 1
                nums[f_index] = nums[s_index]
                s_index = s_index + 1
        for i in range(f_index + 1, len(nums)):
            nums[i] = "_"
        return f_index + 1


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(solution.removeDuplicates([1, 1, 2]))
