from typing import List
import numpy as np


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        score_tracker = [
            [float("-inf") for i in range(len(prices))] for i in range(len(prices))
        ]
        for x in range(len(prices)):
            initial_buy = prices[x]
            for y in range(x + 1, len(prices)):
                score = prices[y] - initial_buy - 2
                score_tracker[x][y] = score
        score_tracker = np.array(score_tracker)
        max_tracker = [
            [float("-inf") for i in range(len(prices))] for i in range(len(prices))
        ]
        ### Find max score
        column_list = []
        for col in np.hsplit(score_tracker, score_tracker.shape[1]):
            column_list.append(col)

        def recur_sol(score, row_ind, col_ind, max_tracker=max_tracker):
            if score[row_ind][col_ind] == float("-inf"):
                return float("-inf")
            if max_tracker[row_ind][col_ind] != float("-inf"):
                return max_tracker[row_ind][col_ind]
            if row_ind >= len(score) - 1:
                return 0
            max_score = score[row_ind][col_ind] + max(
                [recur_sol(score, row_ind + 1, col_ind + i, max_tracker)[0]]
                for i in range(len(score) - col_ind)
            )
            max_tracker[row_ind][col_ind] = max_score
            return max_score, max_tracker

        _temp_max_score, max_tracker = recur_sol(score, 0, 0, max_tracker=max_tracker)
        return max(max(max_tracker),0)


solution = Solution()
print(solution.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
