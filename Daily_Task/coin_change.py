import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def recurse(coins, amount, memoir):
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            if amount in memoir:
                return memoir[amount]
            memoir[amount] = min(
                [recurse(coins, amount - coin, memoir) + 1 for coin in coins]
            )
            return memoir[amount]

        memoir = {}
        result = recurse(coins, amount, memoir)
        return -1 if result == math.inf else result


solution = Solution()
print(solution.coinChange(coins=[1, 2, 5], amount=11))
print(solution.coinChange(coins=[2], amount=3))
print(solution.coinChange(coins=[1], amount=0))
