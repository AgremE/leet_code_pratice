from typing import List
from collections import deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def construct_graph(dislikes):
            graph = {}
            first_vertex = 0
            for v in dislikes:
                v1, v2 = v
                if first_vertex == 0:
                    first_vertex = v1
                if v1 in graph:
                    graph[v1].append(v2)
                else:
                    graph[v1] = [v2]
            return graph, first_vertex

        graph, first_vertex = construct_graph(dislikes)
        grp_1, grp_2 = [first_vertex], graph[first_vertex]
        already_visit = {first_vertex: 1}
        next_visit = graph[first_vertex]
        odd_count = 1
        while next_visit:
            c_v = next_visit.pop()
            if c_v in already_visit:
                continue
            else:
                already_visit[c_v] = 1
            if not (c_v in graph):
                continue
            next_visit = graph[c_v] + next_visit
            if odd_count == 1:
                grp_1 = grp_1 + graph[c_v]
                grp_2 = grp_2 + [c_v]
                odd_count = 0
            else:
                grp_1 = grp_1 + [c_v]
                grp_2 = grp_2 + graph[c_v]
                odd_count = 1
        s_1 = set(grp_1)
        s_2 = set(grp_2)
        return len(s_1 & s_2) == 0, s_1, s_2


solution = Solution()
print(
    solution.possibleBipartition(n=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])
)
print(solution.possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]]))
