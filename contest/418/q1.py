from typing import List
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse=True)
        bin_num = [bin(num)[2:] for num in nums]
        result = ""
        for num in bin_num:
            result+=num
        return int(result,2)
    
solution = Solution()
print(solution.maxGoodNumber( nums = [1,2,3]))