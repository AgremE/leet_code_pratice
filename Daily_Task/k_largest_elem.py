import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            temp = heapq.heappop(heap)
            if nums[i] > temp:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappush(heap, temp)
        return heapq.heappop(heap)


solution = Solution()
print(solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
