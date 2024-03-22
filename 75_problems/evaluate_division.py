from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}
        reverse_graph = {}
        for i in range(len(equations)):
            v1, v2 = equations[i]
            val = values[i]
            if v1 in graph:
                graph[v1].append((v2, val))
            else:
                graph[v1] = [(v2, val)]

            if v2 in graph:
                reverse_graph[v2].append((v1, 1 / val))
            else:
                reverse_graph[v2] = [(v1, 1 / val)]

        def bfs(graph, s_v, e_v):
            n_v = graph[s_v]
            temp_v = []
            tracker = set([s_v])
            while n_v:
                _v, val = n_v.pop()
                if _v == e_v:
                    return val
                tracker.add(s_v)
                if _v in tracker:
                    continue
                tracker.add(_v)
                temp_n_v = graph[_v]
                for tmp_v, tmp_val in temp_n_v:
                    temp_v.append((tmp_v, val * tmp_val))
            return -1

        result = []
        for query in queries:
            s_v, e_v = query
            if s_v in graph:
                result.append(bfs(graph, s_v, e_v))
            elif s_v in reverse_graph:
                result.append(bfs(reverse_graph, s_v, e_v))
            result.append(-1)
        return result
