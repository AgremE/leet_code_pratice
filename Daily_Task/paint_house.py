from typing import List
import math


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])


solution = Solution()
print(solution.minCost(costs=[[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]))
