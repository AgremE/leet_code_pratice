class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##
        # This problem is relatively easy
        # we use XOR to track number use to appear in odd or even
        # at the end we take the list number from both tracker to
        # get the left first positive number
        # #
        len_arr = len(nums)
        if 1 in nums:
            return 1
        for i, num in enumerate(nums):
            if num <= 0:
                continue
            if num > len(nums) - 1:
                continue
            nums[i - 1] = i
