from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        matrice_sum_row = [
            [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))
        ]
        matrice_sum_col = [
            [0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))
        ]

        def transpose(matrix):
            return [list(i) for i in zip(*matrix)]

        def get_sum_matrix(matrix, helper_matrix):
            max_col = len(matrix[0])
            for i_row in range(len(matrix)):
                helper_matrix[i_row][0] = matrix[i_row][0]
                for i_col in range(1, max_col):
                    helper_matrix[i_row][i_col] = (
                        helper_matrix[i_row][i_col - 1] + matrix[i_row][i_col]
                    )
            return helper_matrix

        def get_sum_target(matrix, target):
            max_row = len(matrix)
            result_ = 0
            for _len in range(max_row):
                for i_row in range(len(matrix) - _len):
                    for i_col in range(len(matrix[0])):
                        if (
                            sum([matrix[i_row + i][i_col] for i in range(_len)])
                            == target
                        ):
                            result_ += 1
            return result

        matrice_sum_row = get_sum_matrix(matrix, matrice_sum_row)
        matrice_sum_col = get_sum_matrix(transpose(matrix), matrice_sum_col)

        result = 0
        result += get_sum_target(matrice_sum_row, target)
        result += get_sum_target(matrice_sum_col, target)
        return result


solution = Solution()
print(solution.numSubmatrixSumTarget(matrix=[[1, -1, 1], [-1, 1, 2]], target=0))
