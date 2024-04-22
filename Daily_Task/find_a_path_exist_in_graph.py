from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for v1,v2 in edges:
            if v1 in graph:
                graph[v1].append(v2)
            else:
                graph[v1] = [v2]
            if v2 in graph:
                graph[v2].append(v1)
            else:
                graph[v2] = [v1]
        n_v = [source]
        already_visit = set()
        temp_n_v = []
        while n_v:
            v = n_v.pop()
            temp_n_v = temp_n_v + graph[v]
            if v in already_visit:
                continue
            already_visit.add(v)
            if v == source:
                return True
            if not n_v:
                n_v = temp_n_v
                temp_n_v=[]
        return False
