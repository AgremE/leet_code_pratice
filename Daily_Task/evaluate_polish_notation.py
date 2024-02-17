from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for _i in range(len(tokens) - 1, -1, -1):
            stack.append(tokens[_i])
        num_stack = [int(stack.pop(-1)), int(stack.pop(-1))]
        while stack:
            _m = stack.pop(-1)
            if _m == "+":
                _f = num_stack.pop(-1)
                _s = num_stack.pop(-1)
                num_stack.append(_s + _f)
            elif _m == "-":
                _f = num_stack.pop(-1)
                _s = num_stack.pop(-1)
                num_stack.append(_s - _f)
            elif _m == "*":
                _f = num_stack.pop(-1)
                _s = num_stack.pop(-1)
                num_stack.append(_s * _f)
            elif _m == "/":
                _f = num_stack.pop(-1)
                _s = num_stack.pop(-1)
                num_stack.append(int(_s / _f))
            else:
                num_stack.append(int(_m))
        return num_stack[0]


solution = Solution()
print(solution.evalRPN(tokens=["4", "13", "5", "/", "+"]))
