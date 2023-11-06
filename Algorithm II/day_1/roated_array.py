from posixpath import split
from re import T
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ### Looking for pivotal index in the num after rotating:
        ### Using binary search for the biggest number to the left
        left_i = 0
        right_i = len(nums) - 1
        fake_max = nums[right_i]
        mid_i = 0
        split_i = 0
        is_sorted = False
        if len(nums) == 1 or len(nums) == 2:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1
        ### Should reorder
        if fake_max < nums[0]:
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
            split_i = len(nums[mid_i+1:])
            before_rotate = nums[mid_i+1:]+nums[:mid_i+1]
        else:
            is_sorted = True
            before_rotate = nums
            split_i = 0
        target_i = 0
        left_i = 0
        right_i = len(nums) - 1
        found = False
        while left_i <= right_i:
            target_i = (left_i+right_i)//2 
            num = before_rotate[target_i]
            if num < target:
                left_i = target_i+1
                target_i = (left_i+right_i)//2
            elif num > target:
                right_i = target_i - 1
                target_i = (left_i+right_i)//2
            elif num == target:
                found = True
                break
        if not found:
            return -1     
        if is_sorted:
            return target_i
        if target > fake_max:
            return target_i - split_i
        elif target < fake_max:
            return (len(before_rotate)-split_i) + target_i
        else:
            return len(nums) - 1

test_case_2 =[4,5,6,7,0,1,2]
#test_case_2 = [4,5,6,7,0,1,2]
#test_case_2 = [2,3,4,5,6,7,1]
test_solution = Solution()
print(test_solution.search(test_case_2,0))