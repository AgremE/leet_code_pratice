class Solution:
    def addBinary(self, a: str, b: str) -> str:
        min_len = min(len(a), len(b))
        a, b = a[::-1], b[::-1]
        result = []
        carry = 0
        for i in range(min_len):
            if carry == 0:
                if (a[i] == "1") and (b[i] == "1"):
                    result.append(0)
                    carry = 1
                else:
                    if (a[i] == "1") or (b[i] == "1"):
                        result.append(1)
                    else:
                        result.append(0)
            elif carry == 1:
                if (a[i] == "1") and (b[i] == "1"):
                    result.append(1)
                else:
                    if (a[i] == "1") or (b[i] == "1"):
                        result.append(0)
                    else:
                        result.append(1)
                        carry = 0
        if carry == 1:
            left_part = a[min_len:] + b[min_len:]
            for i in left_part:
                if i == "1":
                    result.append(0)
                else:
                    carry = 0
                    result.append(1)
            if result[-1] == 0:
                result.append(1)
        else:
            left_part = a[min_len:] + b[min_len:]
            for i in left_part:
                result.append(i)
        return "".join([str(x) for x in result[::-1]])


solution = Solution()
print(solution.addBinary(a="1111", b="1111"))
