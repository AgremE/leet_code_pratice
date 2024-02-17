from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def get_max(arr, i, k):
            if i >= k:
                return max(arr[i - k : i + k])
            else:
                return max(arr[: i + k])

        result = 0
        for i in range(len(arr)):
            result += get_max(arr, i, k)
        return result


solution = Solution()
print(solution.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
