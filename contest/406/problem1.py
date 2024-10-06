class Solution:
    def getSmallestString(self, s: str) -> str:
        swap_i = -1
        for i in range(1, len(s)):
            if (abs(int(s[i]) - int(s[i - 1])) % 2 == 0) and (
                int(s[i]) < int(s[i - 1])
            ):
                swap_i = i
                break
        if swap_i == -1:
            return s
        return s[: swap_i - 1] + s[swap_i] + s[swap_i - 1] + s[swap_i + 1 :]


solution = Solution()
print(solution.getSmallestString("453"))
