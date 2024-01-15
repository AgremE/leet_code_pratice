from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def recurv(k, d_i, prices, sale_flag, memoir):
            if (k, d_i) in memoir:
                return memoir[(k, d_i)]
            if k == 1:
                if sale_flag:
                    return max(prices[d_i:])
                else:
                    return 0
            if d_i >= len(prices) - 1:
                if not sale_flag:
                    return 0
                else:
                    return prices[d_i]
            if sale_flag:
                memoir[(k, d_i, sale_flag)] = max(
                    recurv(k, d_i, prices, sale_flag=not sale_flag, memoir=memoir)
                    + prices[d_i],
                    recurv(k, d_i + 1, prices, sale_flag=sale_flag, memoir=memoir),
                )
            else:
                memoir[(k, d_i)] = max(
                    recurv(
                        k - 1, d_i + 1, prices, sale_flag=not sale_flag, memoir=memoir
                    )
                    - prices[d_i],
                    recurv(k, d_i + 1, prices, sale_flag=sale_flag, memoir=memoir),
                )
            return 1

        memoir = {}
        result = recurv(k, 0, prices, False, memoir)
        return result


solution = Solution()
# print(solution.maxProfit(k=1000, prices=[2, 4, 1]))
print(solution.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
