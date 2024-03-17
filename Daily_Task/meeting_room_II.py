from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        heapq.heapify(heap)
        s, e = intervals.pop(0)
        heapq.heappush(heap, (e, s))
        for s, e in intervals:
            h_e, h_s = heapq.heappop(heap)
            if s < h_e:
                heapq.heappush(heap, (h_e, h_s))
                heapq.heappush(heap, (e, s))
            else:
                heapq.heappush(heap, (e, h_s))
        return len(heap)
