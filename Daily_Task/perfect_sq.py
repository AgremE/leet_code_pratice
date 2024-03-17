import math


class Solution:
    def numSquares(self, n: int) -> int:
        def recurv(n, memoir):
            if n in memoir:
                return memoir[n]
            if n < 0:
                return math.inf
            # Check sq
            k = int(n**0.5)
            if n == k**2:
                return 1
            memoir[n] = min([recurv(n - i**2, memoir) + 1 for i in range(1, 101)])
            return memoir[n]

        memoir = {}
        return recurv(n, memoir)


solution = Solution()
print(solution.numSquares(12))
print(solution.numSquares(13))
print(solution.numSquares(14))
