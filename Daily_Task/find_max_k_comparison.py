class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        _mod = 10**9 + 7
        # dp[n][cost][max_value]
        dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0][:] = [1 for x in range(m)]
        for _i in range(1, n):
            for _cost in range(k):
                for _max_value in range(m):
                    # Consider the case that max value has no effect on the search cost
                    dp[_i][_cost][_max_value] = (
                        dp[_i][_cost][_max_value]  # max value itself
                        + (_max_value + 1) * dp[_i - 1][_cost][_max_value]
                    ) % _mod  # mul by max value + 1 because max val and value under itself added to the array
                    if _cost != 0:
                        # Considering the search cost that change from cost - 1 to cost
                        total_sum = 0
                        for pre_max in range(_max_value):
                            total_sum = (
                                total_sum + dp[_i - 1][_cost - 1][pre_max]
                            ) % _mod
                        dp[_i][_cost][_max_value] = (
                            dp[_i][_cost][_max_value] + total_sum
                        ) % _mod
        answer = 0
        for i in range(m):
            answer = (answer + dp[n - 1][k - 1][i]) % _mod
        return answer
