class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        divider = 10**9 + 7
        total = 0
        for i in range(1, m + 1):
            total = total + i ** (n - 1) % divider
        return total


solution = Solution()
print(solution.numOfArrays(n=2, m=3, k=1))
