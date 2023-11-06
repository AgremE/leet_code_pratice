from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        def _construct_graph(n_vertex, relations):
            graph = [[] for x in range(n_vertex + 1)]
            out_degree = [[] for x in range(n_vertex + 1)]
            for x, y in relations:
                graph[y].append(x)
                out_degree[x].append(y)
            end_vertex = []
            for v in range(len(out_degree)):
                next_c = out_degree[v]
                if len(next_c) == 0:
                    end_vertex.append(v)
            return graph, end_vertex

        def _solver(_v, graph, time, memoir):
            if _v in memoir:
                return memoir[_v]
            if graph[_v] == []:
                return time[_v - 1]
            _pre_course = graph[_v]
            memoir[_v] = (
                max([_solver(x, graph, time, memoir) for x in _pre_course])
                + time[_v - 1]
            )
            return memoir[_v]

        graph, end_v = _construct_graph(n, relations)
        memoir = {}
        # all end vertex
        solution = []
        for v in end_v:
            solution.append(_solver(v, graph, time, memoir))
        return max(solution)


solution = Solution()

print(solution.minimumTime(n=2, relations=[[2, 1]], time=[10000, 10000]))
print(solution.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
print(
    solution.minimumTime(
        n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]
    )
)
