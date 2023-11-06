from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total_array_count = 0
        for i in range(len(nums)):
            temp_total_sum = sum(nums[i:])
            if temp_total_sum % k == 0:
                total_array_count = total_array_count + 1
            for j in range(len(nums) - 1, i, -1):
                temp_total_sum = temp_total_sum - nums[j]
                if temp_total_sum % k == 0:
                    total_array_count = total_array_count + 1
        return total_array_count


solution = Solution()
print(solution.subarraysDivByK(nums=[-7, 2, 3, 0, -9], k=3))
