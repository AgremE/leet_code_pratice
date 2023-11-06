from typing import List
import math


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        num_dic = {x: i for i, x in enumerate(arr)}
        dp = [1 for i in range(len(arr))]
        for i, num in enumerate(arr):
            for j in range(i):
                right = num // arr[j]
                if (num % arr[j] == 0) & (right in num_dic):
                    dp[i] = dp[i] + dp[j] * dp[num_dic[right]]
                    dp[i] = dp[i] % (10**9 + 7)
        return sum(dp) % (10**9 + 7)


solution = Solution()
print(solution.numFactoredBinaryTrees(arr=[5, 19, 15, 10]))
print(solution.numFactoredBinaryTrees(arr=[2, 4]))
print(solution.numFactoredBinaryTrees(arr=[2, 4, 5, 10]))
