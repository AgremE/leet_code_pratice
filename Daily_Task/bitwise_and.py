import math


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        if int(math.log2(right)) > int(math.log2(left)):
            return 0
        return int(math.log2(left))


solution = Solution()
print(solution.rangeBitwiseAnd(left=5, right=7))
