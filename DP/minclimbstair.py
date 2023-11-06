from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    l_cost = len(cost)
    result_map = [[0 for x in range(2)] for y in range(l_cost)]
    result_map[0][0] = 0
    result_map[0][1] = cost[0]
    for i in range(1, l_cost):
        result_map[i][0] = result_map[i - 1][1]
        result_map[i][1] = min(
            result_map[i - 1][0] + cost[i], result_map[i - 1][1] + cost[i]
        )
    return min(result_map[l_cost - 1][0], result_map[l_cost - 1][1])


minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
