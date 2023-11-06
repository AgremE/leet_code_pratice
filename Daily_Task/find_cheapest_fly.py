from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        def get_graph(flights):
            graph = {}
            for _fly in flights:
                _f, _d, _p = _fly
                if _f in graph:
                    graph[_f].append((_d, _p))
                else:
                    graph[_f] = [(_d, _p)]
            return graph

        def reachable_at_k_stp(graph, s, k):
            ### Using BFS
            already_visit = {s: 1}
            ls_n_v = graph[s]
            ls_n_n_v = []
            cost = 0
            while ls_n_v:
                n_v = ls_n_v.pop()
