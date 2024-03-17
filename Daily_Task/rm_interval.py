from typing import List


class Solution:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        result = []
        for interval in intervals:
            if (interval[0] < toBeRemoved[0]) and (interval[1] > toBeRemoved[1]):
                result.append([interval[0], toBeRemoved[0]])
                result.append([toBeRemoved[1], interval[1]])
            elif interval[1] < toBeRemoved[0]:
                result.append(interval)
            elif (interval[1] >= toBeRemoved[0]) and (interval[0] < toBeRemoved[0]):
                result.append([interval[0], toBeRemoved[0]])
            elif interval[0] > toBeRemoved[1]:
                result.append(interval)
            elif (interval[0] <= toBeRemoved[1]) and interval[1] > toBeRemoved[1]:
                result.append([toBeRemoved[1], interval[1]])
            elif (interval[0] >= toBeRemoved[0]) and (interval[1] <= toBeRemoved[1]):
                continue
        return result


solution = Solution()
print(
    solution.removeInterval(
        intervals=[[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], toBeRemoved=[-1, 4]
    )
)
