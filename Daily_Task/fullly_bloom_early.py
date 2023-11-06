from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0
        input_loop = sorted(zip(growTime, plantTime))
        for g, p in input_loop:
            ans = g + p if g >= ans else ans + p
        return ans


solution = Solution()
print(solution.earliestFullBloom([1, 4, 3], [2, 3, 1]))
