#from types import List
class Solution:
    def search(self, nums, target: int) -> int:
        mid_idx = len(nums)//2
        upper_b = len(nums)-1
        lower_b = 0
        while True:
            if target == nums[mid_idx]:
                return mid_idx
            elif target < nums[mid_idx]:
                upper_b = mid_idx - 1 
                mid_idx = (upper_b+lower_b)//2
            elif target > nums[mid_idx]:
                lower_b = mid_idx  + 1
                mid_idx = (upper_b+lower_b)//2
            if mid_idx > upper_b or mid_idx<lower_b:
                return -1 

test_obj = Solution()
print(test_obj.search([2,5],2))