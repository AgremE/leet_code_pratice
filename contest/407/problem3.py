class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        list_s = s.split("0")
        list_s = [x for x in list_s if x != ""]
        if s.endswith("1"):
            list_s.pop()
        result = 0
        for i, _s in enumerate(list_s):
            result += len(_s) * (len(list_s) - i)
        if result == 0 and list_s:
            if s.endswith("0"):
                return len(list_s[0])
        return result


solution = Solution()
print(solution.maxOperations("111101100"))
print(solution.maxOperations("1001101"))
print(solution.maxOperations("00111"))
