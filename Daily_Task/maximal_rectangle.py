from typing import List
import math
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        memoir = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        _max_area = -math.inf
        for row_i in range(len(matrix)):
            for col_i in range(len(matrix[0])):
                if matrix[row_i][col_i] == 0:
                    continue
                if col_i>=1:
                    memoir[row_i][col_i] = memoir[row_i][col_i-1]+1
                else:
                    memoir[row_i][col_i] = 1
                width = memoir[row_i][col_i]
                for k in range(row_i,-1,-1):
                    width = min(width,memoir[k][col_i])
                    _max_area = max(_max_area,abs(width*k))
        return _max_area