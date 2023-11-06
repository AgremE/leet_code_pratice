from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ### Working on pivotal value of zero
        ### If there is no negative number/positive number, there should be no zero add up
        left_ind = 0
        right_ind = len(nums)-1
        nums.sort()
        if not nums or nums[0] >= 0 or nums[right_ind] <= 0:
            if len(nums) < 3:
                return []
            else:
                if sum(nums[:3]) == 0 or sum(nums[-3:]) == 0:
                    return [[0,0,0]]
        ### find the middle ground
        mid_ind = 0
        while(left_ind<=right_ind):
            mid_ind = (left_ind+right_ind)//2
            elem = nums[mid_ind]
            if elem == 0:
                break
            elif elem < 0:
                left_ind = mid_ind + 1
            elif elem > 0:
                right_ind = mid_ind - 1
        final_result = []
        ### Finding the set of three element
        pivot = mid_ind
        if pivot + 2 <= len(nums)-1:
            result = nums[pivot]+nums[pivot+1]+nums[pivot+2]
            if result == 0:
                final_result.append([nums[pivot],nums[pivot+1],nums[pivot+2]])
        if pivot - 2 >= 0:
            result = nums[pivot]+nums[pivot-1]+nums[pivot-2]
            if result == 0:
                final_result.append([nums[pivot],nums[pivot-1],nums[pivot-2]])
        ### Fix middle
        next_left = pivot - 1
        next_right = pivot + 1
        while True:
            if next_left < 0 or next_right > len(nums) - 1:
                break
            f_elem,s_elem,t_elem = nums[next_left],nums[pivot],nums[next_right]
            total_sum = f_elem + s_elem + t_elem
            if total_sum == 0:
                final_result.append([f_elem,s_elem,t_elem])
            next_left = next_left - 1
            next_right = next_right + 1

        ### Go left
        left_pivot = pivot
        next_left = pivot - 1
        next_right = pivot + 1
        while True:
            if next_left < 0 or next_right > len(nums) - 1:
                break
            f_elem,s_elem,t_elem = nums[next_left],nums[left_pivot],nums[next_right]
            total_sum = f_elem + s_elem + t_elem
            if total_sum == 0:
                ## Append in result
                next_right = next_right + 1
                if [f_elem,s_elem,t_elem] not in final_result:
                    final_result.append([f_elem,s_elem,t_elem])
            elif total_sum < 0:
                next_right = next_right + 1
            elif total_sum > 0:
                left_pivot = left_pivot - 1
                next_left = next_left - 1
        right_pivot = pivot
        next_left = pivot - 1
        next_right = pivot + 1
        while True:
            if next_left < 0 or next_right > len(nums) - 1:
                break
            f_elem,s_elem,t_elem = nums[next_left],nums[right_pivot],nums[next_right]
            total_sum = f_elem + s_elem + t_elem
            if total_sum == 0:
                ## Append in result
                next_left = next_left - 1
                if [f_elem,s_elem,t_elem] not in final_result:
                    final_result.append([f_elem,s_elem,t_elem])
            elif total_sum < 0:
                right_pivot = right_pivot + 1
                next_right = next_right + 1
            elif total_sum > 0:
                next_left = next_left - 1
        return final_result

test = Solution()
print(test.threeSum([3,0,-2,-1,1,2]))