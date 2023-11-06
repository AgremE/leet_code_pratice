from typing import List
import numpy as np


import numpy as np


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_t = np.array(grid)
        grid_t = np.transpose(grid_t)
        grid = np.array(grid)
        result = 0
        for col in grid_t:
            for row in grid:
                if not np.any(np.subtract(row, col)):
                    result = result + 1
        return result


solution = Solution()
print(solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
