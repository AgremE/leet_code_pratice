from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def recure(nums, multi, num_i, num_j, mul_i, memior):
            if mul_i == len(multi) - 1:
                return max(nums[num_i] * multi[-1], nums[num_j] * multi[-1])
            if (num_i, num_j, mul_i) in memior:
                return memior[(num_i, num_j, mul_i)]
            if num_i == num_j:
                return nums[num_i] * multi[mul_i]
            memior[(num_i, num_j, mul_i)] = max(
                recure(nums, multi, num_i, num_j - 1, mul_i + 1, memior)
                + nums[num_j] * multi[mul_i],
                recure(nums, multi, num_i + 1, num_j, mul_i + 1, memior)
                + nums[num_i] * multi[mul_i],
            )
            return memior[(num_i, num_j, mul_i)]

        memoir = {}
        result = recure(nums, multipliers, 0, len(nums) - 1, 0, memoir)
        return result


solution = Solution()
print(solution.maximumScore(nums=[1, 2, 3], multipliers=[3, 2, 1]))
print(
    solution.maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6])
)
