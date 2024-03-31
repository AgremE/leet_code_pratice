from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def recurv(nums, i, k, cur_count=0, memior={}):
            if (i, k) in memior:
                return memior[(i, k)]
            if k == 0:
                return cur_count
            if i == len(nums):
                return cur_count
            memior[(i, k)] = (
                recurv(nums, i, k, cur_count + 1, memior)
                if nums[i] == 1
                else max(
                    [
                        recurv(nums, i + 1, k - 1, cur_count + 1, memior),
                        recurv(nums, i + 1, k, 0, memior),
                    ]
                )
            )
            return memior[(i, k)]

        memoir = {}
        return recurv(nums, 0, k, 0, memior=memoir)
