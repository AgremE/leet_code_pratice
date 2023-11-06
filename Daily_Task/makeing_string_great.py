class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            not_found = True
            for i in range(1, len(s)):
                if (s[i].lower() == s[i - 1].lower()) and (
                    (s[i].islower() and s[i - 1].isupper())
                    or (s[i].isupper() and s[i - 1].islower())
                ):
                    s = s[: i - 1] + s[i + 1 :]
                    not_found = False
                    break
            if not_found:
                break
        if (
            (len(s) == 2)
            and (s[0].lower() == s[1].lower())
            and (
                (s[0].islower() and s[1].isupper())
                or (s[0].isupper() and s[1].islower())
            )
        ):
            return ""
        return s


solution = Solution()
# print(solution.makeGood("leEeetcode"))
print(solution.makeGood("AQq"))
