import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Memoir here is two dimensional array that store information about
        # wheather the selling is much better than buying on that day
        # this depend pretty much the prevoius day action that we perform
        def recurv(prices, fee, day, memoir, buy):
            if buy:
                if day >= len(prices):
                    return max(fee, prices[-1])
                if memoir[day][1] != -math.inf:
                    return memoir[day][1]
                memoir[day][1] = max(
                    recurv(prices, fee, day + 1, memoir, buy),
                    recurv(prices, fee, day + 1, memoir, not buy) + prices[day],
                )
                return memoir[day][1]
            else:
                if day >= len(prices):
                    return 0
                if memoir[day][0] != -math.inf:
                    return memoir[day][0]
                memoir[day][0] = max(
                    recurv(prices, fee, day + 1, memoir, buy),
                    recurv(prices, fee, day + 1, memoir, not buy) - (prices[day] + fee),
                )
                return memoir[day][0]

        memoir = [[-math.inf for _ in range(2)] for _ in range(len(prices))]
        result = recurv(prices, fee, 0, memoir, False)
        return result


soltuion = Solution()
print(soltuion.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
