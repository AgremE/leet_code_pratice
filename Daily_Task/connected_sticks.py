from typing import List
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        tracker = []
        if len(sticks) < 2:
            if len(sticks) == 1:
                return 0
            return sum(sticks)
        heapq.heapify(tracker)
        for _s in sticks:
            heapq.heappush(tracker, _s)
        cost = 0
        while len(tracker) > 1:
            f_s = heapq.heappop(tracker)
            s_s = heapq.heappop(tracker)
            temp_cost = f_s + s_s
            cost += temp_cost
            heapq.heappush(tracker, temp_cost)
        return cost


solution = Solution()
print(
    solution.connectSticks(
        sticks=[3354, 4316, 3259, 4904, 4598, 474, 3166, 6322, 8080, 9009]
    )
)
