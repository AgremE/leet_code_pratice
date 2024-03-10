from typing import List
import math

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = {}
        for s,d,p in flights:
            if s in graph:
                graph[s].append([d,p])
            else:
                graph[s] = [[d,p]]
        n_v_ls = graph[src]
        distances = [math.inf for _ in range(n)]
        _cur_p = 0
        for _ in range(k+1):
            _level = n_v_ls
            n_v_ls = []
            while _level:
                d,p  = _level.pop()
                for nei,w in graph[d]:
                    if w + p < distances[nei]:
                        distances[nei] = w + p
                        n_v_ls.append((d,p+w))
        return -1 if distances[dst]==math.inf else distances[dst]
            