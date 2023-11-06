class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divided(_str, _divisor):
            test = ("").join(_str.split(_divisor))
            if test == "":
                return True
            return False

        if len(str1) > len(str2):
            divisor = str2
            finder = str1
        else:
            divisor = str1
            finder = str2
        result = ""
        for i in range(len(divisor)):
            for j in range(i + 1, len(divisor) + 1):
                _d = divisor[i:j]
                if _d:
                    if is_divided(finder, _d) and is_divided(divisor, _d):
                        if len(_d) > len(result):
                            result = _d
        return result


solution = Solution()
print(solution.gcdOfStrings("ABCABC", str2="ABC"))
