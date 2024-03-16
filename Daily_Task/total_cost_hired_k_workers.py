from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = []
        right_heap = []
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        for i in range(k):
            if len(costs)>1:
                heapq.heappush(left_heap,costs[0])
                heapq.heappush(right_heap,costs[-1])
                del costs[0]
                del costs[-1]
            elif costs:
                heapq.heappush(left_heap,costs[0])
                del costs[0]
        total_cost = 0
        for i in range(k):
            left_val,right_val = math.inf,math.inf
            if left_heap:
                left_val = heapq.heappop(left_heap)
            if right_heap:
                right_val = heapq.heappop(right_heap)
            if right_val > left_val:
                heapq.heappush(right_heap,right_val)
                if costs:
                    heapq.heappush(left_heap,costs[-1])
                    del costs[-1]
                total_cost+=left_val
            else:
                heapq.heappush(right_heap,left_val)
                if costs:
                    heapq.heappush(left_heap,costs[0])
                    del costs[0]
                total_cost+=right_val
        return total_cost


soltuion = Solution()
print(
    soltuion.totalCost(
        costs=[31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58],
        k=11,
        candidates=2,
    )
)
