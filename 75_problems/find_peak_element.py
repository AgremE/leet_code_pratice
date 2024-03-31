from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # using the binary searh to perform such action
        if len(nums) < 3 and len(nums) > 1:
            return nums.index(max(nums))
        if len(nums) == 1:
            return 0
        l_b = 0
        h_b = len(nums) - 1

        while l_b < h_b:
            mid = (h_b + l_b) // 2
            if (h_b == mid) or (l_b == mid):
                if nums[h_b] > nums[l_b]:
                    return h_b
                return l_b
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                h_b = mid
            elif nums[mid] < nums[mid + 1]:
                l_b = mid
            if (mid == len(nums) - 1) or (mid == 0):
                return mid


solution = Solution()
print(solution.findPeakElement(nums=[1, 2, 3]))
