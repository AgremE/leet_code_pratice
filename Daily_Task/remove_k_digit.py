class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # using monotonic increasing sequqence to solve this problem
        stack = []
        for _n in num:
            while (k > 0 and stack) and (stack[-1] > _n):
                stack.pop()
                k -= 1
            stack.append(_n)
        stack = stack[:-k] if k else stack
        str_num = "".join(stack)
        if str_num == "":
            return "0"
        return str(int(str_num))


solution = Solution()
# print(solution.removeKdigits("52660469",2))
print(solution.removeKdigits("10001", 4))
