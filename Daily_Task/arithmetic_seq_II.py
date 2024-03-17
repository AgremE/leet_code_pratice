from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # make matrix that construct and a good different of sequence
        # then count the one with consitent different and the one with zero different
        diff_list = []
        for i in range(len(nums)):
            temp = []
            for j in range(i + 1, len(nums)):
                temp.append(nums[j] - nums[i])
            diff_list.append(temp)
