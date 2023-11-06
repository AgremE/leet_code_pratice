from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                x = j - i
                y = min([height[i], height[j]])
                current_water = x * y
                if current_water > max_water:
                    max_water = current_water
        return max_water

    ### Considering two point solution that move the advantage of higher wall with
    ### Sacrifying of the distance between the two walls


solution = Solution()

print(solution.maxArea(height=[1, 1]))
