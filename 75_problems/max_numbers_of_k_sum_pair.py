from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        s_i, f_i = 0,len(nums)-1
        total_sum =  nums[s_i] +  nums[f_i]
        count = 0 
        while s_i<f_i:
            if total_sum>k:
               total_sum-=nums[f_i]
               f_i-=1
               total_sum+=nums[f_i]
            elif total_sum < k:
               total_sum-=nums[s_i]
               s_i+=1
               total_sum+=nums[s_i]
            else:
                count+=1
                total_sum-=nums[s_i]
                s_i+=1
                total_sum+=nums[s_i]
        return count
    
solution = Solution()
print(solution.maxOperations(nums = [3,1,3,4,3], k = 6))