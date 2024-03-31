from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # using sliding window
        max_count = 0
        start = 0
        ans = 0
        _max = max(nums)
        for end in range(len(nums)):
            if nums[end] == _max:
                max_count += 1
            while max_count >= k:
                if nums[start] == _max:
                    max_count -= 1
                start += 1
            ans += start
        return ans


soltuion = Solution()
print(soltuion.countSubarrays([1, 3, 2, 3, 3], 2))
