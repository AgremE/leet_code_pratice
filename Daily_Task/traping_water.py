from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Algorithm have to work on monotonic stack
        # stack elem is list of three basic element
        stack = []
        ans = 0
        for i, h in enumerate(height):
            if stack:
                while stack and (h >= height[stack[-1][1]]):
                    elem = stack.pop()
                    water_h = h - elem[1]
                    width = i - elem[0] - 1
                    ans += width * water_h
                    if not stack:
                        break
            else:
                stack.append([i, h])
        return ans
