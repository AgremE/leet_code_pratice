from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        len_row = len(rowSum)
        len_col = len(colSum)
        curr_sum_row = [0 for _ in range(len_row)]
        curr_sum_col = [0 for _ in range(len_col)]

        matrix = [[0 for _ in range(len_col)] for _ in range(len_row)]

        for i in range(len_row):
            for j in range(len_col):
                val = min(rowSum[i] - curr_sum_row[i], colSum[i] - curr_sum_col[i])
                matrix[i][j] = val
                curr_sum_row[i] += val
                curr_sum_col[j] += val
        return matrix
