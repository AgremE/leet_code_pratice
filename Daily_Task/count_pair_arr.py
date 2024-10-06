from typing import List


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff_arr = [x[0] - x[1] for x in zip(nums1, nums2)]
        diff_arr = sorted(diff_arr)
        left_i = 0
        right_i = len(diff_arr) - 1
        res = 0
        while left_i != right_i:
            _sum = diff_arr[left_i] + diff_arr[right_i]
            if _sum > 0:
                res += right_i - left_i
                right_i -= 1
            else:
                left_i += 1
        return res
