from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        result = 0

        def generate_n_col(col, len_col):
            result = [col + i for i in range(-1, 2)]
            result = [x for x in result if 0 <= x and x <= len_col - 1]
            return result

        def recurve(matrix, row, col, memoir):
            if (row, col) in memoir:
                return memoir[(row, col)]
            if row == len(matrix) - 1:
                return matrix[row][col]
            memoir[(row, col)] = min(
                [
                    recurve(matrix, row + 1, gen_col, memoir) + matrix[row][col]
                    for gen_col in generate_n_col(col, len(matrix[0]))
                ]
            )
            return memoir[(row, col)]

        memoir = {}
        result = []
        for col in range(len(matrix[0])):
            memoir[(0, col)] = recurve(matrix, 0, col, memoir)
            result.append(memoir[(0, col)])

        return min(result)


solution = Solution()
print(solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
