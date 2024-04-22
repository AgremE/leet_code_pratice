from typing import List 
import math
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s_i,f_i = 0,0
        count_one = 0 
        use_deleted = False
        _max = -math.inf
        while f_i<len(nums):
            if nums[f_i]==1:
                count_one+=1
                f_i+=1
            else:
                if use_deleted:
                    while s_i<=f_i:
                        if nums[s_i] == 0:
                            use_deleted = False
                            s_i+=1
                            break
                        s_i+=1
                        count_one-=1
                else:
                    f_i+=1
                    use_deleted = True
            _max = max(_max,count_one)
        if _max == len(nums):
            return _max -1
        return _max
solution = Solution()
print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))