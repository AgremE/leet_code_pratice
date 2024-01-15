from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def recurv(k, prices, i, j, memoir):
            if (i, j) in memoir:
                return memoir[(i, j)]
            if k == 0 or i >= len(prices) - 1 or i == j or j >= len(prices):
                return 0
            memoir[(i, j)] = max(
                [
                    recurv(k - 1, prices, j, j_sell, memoir) + (prices[i] - prices[j])
                    for j_sell in range(j + 1, len(prices) + 1)
                ]
            )
            return memoir[(i, j)]

        result = []
        for j in range(1, len(prices)):
            memoir = {}
            result.append(recurv(k, prices, 0, j, memoir))
        return max(result)


solution = Solution()
print(solution.maxProfit(k=2, prices=[2, 4, 1]))
print(solution.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
