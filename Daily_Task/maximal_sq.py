from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def fill_squre(x, y, max_x, max_y, pos_val, matrix, inital_matrix):
            if pos_val == 0:
                return 0
            if x == 0 or y == 0:
                return int(inital_matrix[x][y])
            elif (
                matrix[x - 1][y] == 0
                or matrix[x][y - 1] == 0
                or matrix[x - 1][y - 1] == 0
            ):
                return 0
            elif (
                (matrix[x - 1][y] == matrix[x - 1][y - 1])
                & (matrix[x][y - 1] == matrix[x - 1][y - 1])
                & (matrix[x - 1][y] == matrix[x][y - 1])
            ):
                if pos_val == 0:
                    return 0
                else:
                    return matrix[x - 1][y - 1] + pos_val
            else:
                return max([matrix[x - 1][y], matrix[x - 1][y - 1], matrix[x][y - 1]])

        len_x = len(matrix)
        len_y = len(matrix[0])
        result = [[0] * len_y for _ in range(len_x)]
        for x in range(len_x):
            for y in range(len_y):
                result[x][y] = fill_squre(
                    x, y, len_x, len_y, int(matrix[x][y]), result, matrix
                )
        return max([max(x) for x in result]) ** 2


solution = Solution()
print(
    solution.maximalSquare(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "1"],
        ]
    )
)
