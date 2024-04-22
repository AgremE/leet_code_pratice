from typing import List
import math
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # two pointers 
        s_i,f_i = 0,0
        _max = -math.inf
        while f_i<len(nums):
            if nums[f_i]==1:
                _max = max(_max,f_i-s_i+1)
                f_i+=1
            else:
                if k<=0:
                    while s_i<=f_i:
                        if nums[s_i] == 0:
                            s_i+=1
                            k+=1
                            break
                        s_i+=1
                else:
                    _max = max(_max,f_i-s_i+1)
                    f_i+=1
                    k-=1
        return _max

solution = Solution()
print(solution.longestOnes([0,0,0,1],4))