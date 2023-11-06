from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        len_num = len(nums)
        left_ind = 0
        right_ind = len_num - 1
        fake_largest = nums[right_ind]
        if fake_largest < nums[0]:
            while(left_ind<=right_ind):
                mid_ind = (left_ind + right_ind)//2
                mid_num = nums[mid_ind]
                if mid_ind == 0:
                    return nums[1]
                elif mid_ind == len_num -1:
                    return nums[len_num -1]

                if mid_num  > fake_largest:
                    ## Move right
                    left_ind = mid_ind + 1
                elif mid_num < fake_largest:
                    ## Move left
                    right_ind = mid_ind - 1
                else:
                    break
            return nums[mid_ind]
        else:
            return nums[0]

test = Solution()
print(test.findMin([3,4,5,1,2]))
print(test.findMin([4,5,1,2,3]))
print(test.findMin([4,5,6,7,0,1,2]))
print(test.findMin([4,5,6,7,0]))
#print(test.findMin([11,13,15,17]))
#print(test.findMin([3,1,2]))
