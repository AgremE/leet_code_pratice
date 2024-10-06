from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        _max = max(nums)
        _longest = 0
        count = 0
        for num in nums:
            if num == _max:
                count+=1
            else:
                count = 0
                _longest = max(_longest,count)
        return max(_longest,count)