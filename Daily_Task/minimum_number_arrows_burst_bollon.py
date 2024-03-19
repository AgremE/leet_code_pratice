from typing import List
import heapq


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # the problem can translate into a graph problem which
        # try to find the number of connected componeent that construct
        # from list of points
        heap = []
        heapq.heapify(heap)
        for s, e in points:
            heapq.heappush(heap, (s, e))
        result = 0
        while heap:
            f_s, f_e = heapq.heappop(heap)
            s_s, s_e = heapq.heappop(heap)
            if f_e >= s_s or ((s_e >= f_e) and (f_e >= s_s)):
                heapq.heappush(heap, (s_s, min(f_e, s_e)))
            else:
                result += 1
                heapq.heappush(heap, (s_s, s_e))
        return result


solution = Solution()
print(solution.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
