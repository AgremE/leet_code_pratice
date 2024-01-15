from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time_reach = [0 for i in range(n)]
        for i in range(n):
            reminder = 1 if dist[i] % speed[i] != 0 else 0
            time_reach[i] = dist[i] // speed[i] + reminder
        time_reach = sorted(time_reach)
        for i in range(n):
            if i == 0:
                continue
            if time_reach[i] <= i:
                return i
        return n


solution = Solution()

print(solution.eliminateMaximum([3, 2, 4], [5, 3, 2]))
print(solution.eliminateMaximum([3, 5, 7, 4, 5], [2, 3, 6, 3, 2]))
