from typing import List
import math


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        def recurr(jobs, d, j, list_job, memoir):
            if d < 0:
                return math.inf
            if d == 0:
                if j <= len(jobDifficulty):
                    return max(jobDifficulty[j - 1 :])
                return math.inf
            if d > 0 and j >= len(jobs):
                return math.inf
            if (d, j) in memoir:
                return memoir[(d, j)]
            memoir[(d, j)] = min(
                recurr(jobs, d - 1, j + 1, [jobs[j]], memoir) + max(list_job),
                recurr(jobs, d, j + 1, list_job + [jobs[j]], memoir),
            )
            return memoir[(d, j)]

        memoir = {}
        result = recurr(jobDifficulty, d - 1, 1, [jobDifficulty[0]], memoir)
        return -1 if result == math.inf else result


solution = Solution()
# print(solution.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
print(solution.minDifficulty(jobDifficulty=[1, 1, 1], d=3))
print(solution.minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6))
