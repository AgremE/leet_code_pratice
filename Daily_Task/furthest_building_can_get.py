import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # first exhuast  ladder
        min_heap = []
        heapq.heapify(min_heap)
        if ladders == 0:
            _far = 0
            for i in range(1, len(heights)):
                bricks -= heights[i] - heights[i - 1]
                if bricks < 0:
                    break
                else:
                    _far += 1
            return _far
        if ladders == len(heights) - 1:
            return ladders
        dont_use_res = 0
        _count = 0
        for i in range(len(heights)):
            if heights[i + 1] - heights[i] > 0:
                heapq.heappush(min_heap, heights[i + 1] - heights[i])
                _count += 1
                if _count == ladders:
                    break
            else:
                dont_use_res += 1
        num_replace_ladder = 0
        while min_heap:
            bricks -= heapq.heappop(min_heap)
            if bricks > 0:
                for i in range(ladders + num_replace_ladder, len(heights)):
                    diff_h = (
                        heights[ladders + num_replace_ladder]
                        - heights[ladders + num_replace_ladder - 1]
                    )
                    if diff_h > 0:
                        heapq.heappush(
                            min_heap,
                            diff_h,
                        )
                        num_replace_ladder += 1
                        break
                    else:
                        dont_use_res += 1
            else:
                import heapq


import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []  # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue
            # Otherwise, we will need to take a climb out of ladder_allocations
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1
