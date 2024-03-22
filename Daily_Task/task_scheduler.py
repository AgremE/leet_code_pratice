from typing import List
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = []
        heapq.heapify(heap)
        for k, c in counter.items():
            heapq.heappush(heap, -c)
        total = 0
        cycle = n
        while cycle > 0 and heap:
            temp_count = 0
            temp_store = []
            while cycle > 0 and heap:

                val = -heapq.heappop(heap)
                if val > 1:
                    temp_store.append(-(val + 1))
                temp_count += 1
                cycle -= 1
            if temp_store:
                for val in temp_store:
                    heapq.heappush(heap, val)
            total += temp_count if not heap else n + 1
        return total


solution = Solution()
print(
    solution.leastInterval(
        tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=1
    )
)
