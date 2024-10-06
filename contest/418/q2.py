from typing import List
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = {}
        for a,b in invocations:
            graph[a] = graph.get(a,set([]))
            graph[a].add(b)
        next_v = set(graph.get(k,[]))
        all_sup = set([k])
        already_visit = set([])
        while next_v:
            v = next_v.pop()
            if v not in all_sup:
                all_sup.add(v)
            if v in already_visit:
                continue
            already_visit.add(v)
            for _v in graph.get(v,[]):
                next_v.add(_v)
        for v,sub_graph in graph.items():
            if v in all_sup:
                continue
            for v in sub_graph:
                if v in all_sup:
                    return [x for x in range(n)]
        return [x for x in range(n) if x not in all_sup]
            
                
    
solution = Solution()
print(solution.remainingMethods(4,1, [[1,2],[0,1],[3,2]]))
print(solution.remainingMethods(3,2, [[1,2],[0,1],[2,0]]))