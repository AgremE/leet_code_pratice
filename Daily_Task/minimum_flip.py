class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count("1") + bin(((a & b) & ((a | b) ^ c))).count("1")


solution = Solution()
print(solution.minFlips(a=2, b=6, c=5))
print(solution.minFlips(a=4, b=2, c=7))
print(solution.minFlips(a=1, b=2, c=3))
