import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.tracker = set()
        self.heap = []
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        result = heapq.heappop(self.heap)
        if result in self.tracker:
            del self.tracker.remove(result)
        return result

    def addBack(self, num: int) -> None:
        if num in self.tracker:
            return None
        else:
            heapq.heappush(self.heap,num)
            self.tracker.add(num)