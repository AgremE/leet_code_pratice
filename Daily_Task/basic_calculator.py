from collections import deque


class Solution:
    def cal_expression(self, list_elem) -> int:
        temp_result = []
        next = 1
        for i in range(0, len(list_elem)):
            if list_elem[i] == "-":
                next = next * (-1)
                continue
            elif list_elem[i] == "+":
                continue
            temp_result.append(int(list_elem[i]) * next)
            next = 1
        return sum([int(x) for x in temp_result])

    def calculate(self, s: str) -> int:
        stack = deque()
        temp_result = deque()
        for i in s:
            if i == ")":
                while stack:
                    elem = stack.pop()
                    if elem == "(":
                        break
                    temp_result.appendleft(elem)
                stack.append(self.cal_expression(temp_result))
                temp_result = deque()
                continue
            if i == " ":
                continue
            stack.append(i)
        final_result_temp = deque()
        while stack:
            final_result_temp.appendleft(stack.pop())
        return self.cal_expression(final_result_temp)


solution = Solution()
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))
print(solution.calculate(" 2-1 + 2 "))
print(solution.calculate("1 + 1"))
