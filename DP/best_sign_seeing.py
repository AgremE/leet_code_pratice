from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_left = 0
        for i in range(len(values)):
            score = max_left + values[i] - i
            max_score = max(max_score, score)
            max_left = max(max_left, values[i] + i)
        return max_score


solution = Solution()
print(solution.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
print(solution.maxScoreSightseeingPair([1, 2]))
