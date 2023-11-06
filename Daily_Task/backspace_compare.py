class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        skip = 0
        f_string = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "#":
                skip = skip + 1
            elif skip > 0:
                skip = skip - 1
            else:
                f_string.append(s[i])
        skip = 0
        s_string = []
        for i in range(len(t) - 1, -1, -1):
            if t[i] == "#":
                skip = skip + 1
            elif skip > 0:
                skip = skip - 1
            else:
                s_string.append(t[i])
        if len(f_string) != len(s_string):
            return False
        else:
            for i in range(len(f_string)):
                if f_string[i] != s_string[i]:
                    return False
            return True


solution = Solution()
print(solution.backspaceCompare(s="bxj##tw", t="bxo#j##tw"))
