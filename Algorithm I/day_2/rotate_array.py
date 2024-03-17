class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_arr = len(nums)
        while len_arr < k:
            k = k - len_arr
        f_h = nums[-k:]
        s_h = nums[: k + 1]
        return f_h + s_h


test_solution = Solution()
print(test_solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))
