from typing import List
from math import factorial


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def get_coeffiecent(n, k):
            return factorial(n) / (factorial(k) * factorial(n - k))

        result = []
        for i in range(rowIndex + 1):
            result.append(get_coeffiecent(rowIndex, i))
        return [int(x) for x in result]


solution = Solution()
print(solution.getRow(3))
print(solution.getRow(1))
print(solution.getRow(0))
