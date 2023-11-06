from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find_root(x, roots):
            if x == roots[x]:
                return roots[x]
            roots[x] = find_root(roots[x], roots)
            return roots[x]

        def union(x, y, roots):
            root_x = find_root(x, roots)
            root_y = find_root(y, roots)
            if root_x != root_y:
                roots[root_y] = root_x
            return roots

        roots = [i for i in range(n)]
        for conn in edges:
            roots = union(conn[0], conn[1], roots)
        return sum([1 if x == roots[x] else 0 for x in range(len(roots))])
