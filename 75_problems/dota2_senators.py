import heapq
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        heap_r = []
        heap_d = []
        n = len(senate)
        for i,sen in enumerate(senate):
            if sen == "R":
                heapq.heappush(heap_r,i)
            if sen == "D":
                heapq.heappush(heap_d, i)
        while heap_d and heap_r:
            _d = heapq.heappop(heap_d)
            _r = heapq.heappop(heap_r)
            if _d >_r:
                heapq.heappush(heap_r,_r+n)
            else:
                heapq.heappush(heap_d,_d+n)
        if heap_d:
            return "Dire"
        if heap_r:
            return "Radiant"

soltuion = Solution()
print(soltuion.predictPartyVictory("DRRDRDRDRDDRDRDR"))