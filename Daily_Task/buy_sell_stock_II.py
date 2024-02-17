from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #
        # Let try to solve this problem with DP later
        #
        f_d = 0
        s_d = 1
        result = 0
        while s_d <= len(prices) - 1 and f_d <= len(prices) - 1:
            if prices[f_d] > prices[s_d]:
                f_d += 1
                s_d = f_d + 1
            elif prices[f_d] <= prices[s_d]:
                while True:
                    s_d += 1
                    if prices[s_d - 1] > prices[s_d]:
                        s_d -= 1
                        result += prices[s_d] - prices[f_d]
                        f_d = s_d
                        s_d += 1
                        break
                    elif s_d == len(prices) - 1:
                        result += prices[s_d] - prices[f_d]
                        s_d += 1
                        break
        return result


solution = Solution()
# print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
