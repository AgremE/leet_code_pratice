from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        decrease_h = []
        for i in range(1, len(height)):
            decrease_h.append(height[i] - height[i - 1])
        print(decrease_h)


solution = Solution()
solution.trap([4, 2, 0, 3, 2, 5])
