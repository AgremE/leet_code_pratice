from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ### Insert new interval to existing
        for ind in range(len(intervals)):
            s_val, _ = intervals[ind]
            if s_val > newInterval[0]:
                intervals = intervals[:ind] + [newInterval] + intervals[ind:]
                break
        ## Start the merging process
        ind_to_merge = []
        for ind in range(len(intervals)):
            s_v, e_v = intervals[ind]
            if s_v <= newInterval[0] and newInterval[0] <= e_v:
                ind_to_merge.append(ind)
            if s_v <= newInterval[1] and newInterval[1] <= e_v:
                ind_to_merge.append(ind)
            if newInterval[0] <= s_v and s_v <= newInterval[1]:
                ind_to_merge.append(ind)
            if newInterval[0] <= e_v and e_v <= newInterval[1]:
                ind_to_merge.append(ind)
        min_ind = min(ind_to_merge)
        max_ind = max(ind_to_merge)
        s_val_merge = intervals[min_ind][0]
        e_val_merge = intervals[max_ind][1]
        return (
            intervals[:min_ind]
            + [[s_val_merge, e_val_merge]]
            + intervals[max_ind + 1 :]
        )


solution = Solution()
# print(solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(
    solution.insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    )
)
