from collections import deque


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def isEelem(input: str):
            if input[0].isupper():
                return True
            return False

        def combine_dict(dict1, dict2):
            dict1.update(dict2)
            for key in dict2.keys():
                dict1[key] += dict2[key]
            return dict1

        stack = deque([])
        dict_result = {}
        for i in range(len(formula) - 1, -1, -1):
            c = formula[i]
            if c != "(":
                stack.append(c)
            else:
                last_elem = stack.popleft()
                if last_elem == ")":
                    coeff = 1
                else:
                    coeff = int(last_elem)
                while stack:
                    elem = stack.pop()


solution = Solution()
test_cases = ["H2O", "Mg(OH)2", "K4(ON(SO3)2)2"]
for case in test_cases:
    print(solution.countOfAtoms(case))
