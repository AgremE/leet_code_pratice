from typing import List
import math


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        _max = -math.inf
        _max_area = -math.inf
        for h, w in dimensions:
            if (h**2 + w**2) ** 0.5 > _max:
                _max = (h**2 + w**2) ** 0.5
                _max_area = h * w
            elif (h**2 + w**2) ** 0.5 == _max:
                if h * w >= _max_area:
                    _max_area = h * w
        return _max_area


solution = Solution()
print(
    solution.areaOfMaxDiagonal(
        dimensions=[[6, 5], [8, 6], [2, 10], [8, 1], [9, 2], [3, 5], [3, 5]]
    )
)
