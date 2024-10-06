from typing import List
import heapq
import math


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        """
        Using original to changed as connected edge
        cost is cost of  travelling from origin to chanage v
        then using distrajk to compute the shorted parth from source to target
        if you cannot reach fromm source chart to target char in search graph
        return -1
        """
        graph = {}

        def _construct_graph(edges):
            graph = {}
            for v1, v2, cost in edges:
                graph[v1] = graph.get(v1, [])
                graph[v1].append((v2, cost))
            return graph

        def _distrajk(graph, sv):
            already_visit = set([])
            if sv not in graph:
                return -1
            else:
                result = [math.inf for _ in range(25)]
                q = [(_cost, v) for v, _cost in graph[sv]]
                already_visit.add(sv)
                heapq.heapify(q)
                while q:
                    c, v = heapq.heappop(q)
                    if v in already_visit:
                        continue
                    already_visit.add(v)
                    n_v = graph.get(v, [])
                    for v2, c2 in n_v:
                        if v2 not in result:
                            result[v2] = c + c2
                        else:
                            result[v2] = min(c + c2, c)
