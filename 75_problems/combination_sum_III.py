from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        complete_result = []

        def backtrack(remining, result, n_m):
            if remining == 0 and len(result) == k:
                complete_result.append(result.copy())
            if remining < 0 or len(result) > k:
                return None
            for _m in range(n_m, 9):
                result.append(_m + 1)
                backtrack(remining - _m - 1, result, _m + 1)
                result.pop()

        backtrack(n, [], 0)
        return complete_result


soltuion = Solution()
print(soltuion.combinationSum3(k=3, n=7))
print(soltuion.combinationSum3(k=3, n=9))
