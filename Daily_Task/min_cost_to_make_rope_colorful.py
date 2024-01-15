from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i_ind = 0
        f_ind = 1
        track_dup = [[neededTime[0]]]
        while f_ind < len(colors):
            if colors[i_ind] == colors[f_ind]:
                track_dup[-1].append(neededTime[f_ind])
            else:
                track_dup.append([neededTime[f_ind]])
                i_ind = f_ind
            f_ind += 1
        _min = 0
        for row in track_dup:
            if len(row) > 1:
                _min += sum(sorted(row)[:-1])
        return _min


solution = Solution()
print(solution.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
print(solution.minCost(colors="abc", neededTime=[1, 2, 3]))
print(solution.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
