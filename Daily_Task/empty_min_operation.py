from typing import List
import collections
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        collect = collections.Counter(nums)

        def get_optimal_operation(num):
            if num == 1:
                return math.inf
            if num % 3 == 0:
                return num // 3
            elif num % 3 == 1:
                if num >= 4:
                    return (num - 4) // 3 + 2
                else:
                    return num // 2
            elif num % 3 == 2:
                return num // 3 + (num % 3) // 2

        result = 0
        for num, _count in collect.items():
            result += get_optimal_operation(_count)
        return -1 if result == math.inf else result


solution = Solution()
print(solution.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(solution.minOperations(nums=[2, 1, 2, 2, 3, 3]))
