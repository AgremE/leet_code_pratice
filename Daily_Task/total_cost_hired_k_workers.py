from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = []
        right_heap = []
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        for cost_left in costs[:candidates]:
            heapq.heappush(left_heap, cost_left)
        for cost_right in costs[-candidates:]:
            heapq.heappush(right_heap, cost_right)
        total_cost = 0
        len_cost = len(costs)
        left_ind = candidates - 1
        right_ind = len_cost - candidates
        for i in range(1, k + 1):
            if len_cost - i < candidates:
                total_cost = total_cost + heapq.heappop(left_heap)
                continue
            min_left = heapq.heappop(left_heap)
            min_right = heapq.heappop(right_heap)
            if min_left <= min_right:
                total_cost = total_cost + min_left
                left_ind = left_ind + 1
                heapq.heappush(left_heap, costs[left_ind])
                heapq.heappush(right_heap, min_right)
            else:
                total_cost = total_cost + min_right
                right_ind = right_ind - 1
                heapq.heappush(right_heap, costs[right_ind])
                heapq.heappush(left_heap, min_left)
        return total_cost


soltuion = Solution()
print(
    soltuion.totalCost(
        costs=[31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58],
        k=11,
        candidates=2,
    )
)
