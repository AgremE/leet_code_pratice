class Solution:
    def findMin(self, nums: List[int]) -> int:
        while left_i <= right_i:
                mid_i = (left_i+right_i)//2 
                num = nums[mid_i]
                if num > fake_max:
                    left_i = mid_i+1
                    mid_i = (left_i+right_i)//2
                elif num < fake_max:
                    right_i = mid_i - 1
                    mid_i = (left_i+right_i)//2
                elif num == fake_max:
                    mid_i = mid_i - 1
                    break
            split_i = mid_i
            before_rotate = nums[mid_i+1:]+nums[:mid_i+1]