from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # algorithm
        # using union set
        alice_set = DisjoinSet(n)
        bob_set = DisjoinSet(n)
        num_edge = 0
        for t, v1, v2 in edges:
            if t == 3:
                num_edge += alice_set.union(v1, v2) | bob_set.union(v1, v2)
        for t, v1, v2 in edges:
            if t == 1:
                num_edge += alice_set.union(v1, v2)
            elif t == 2:
                num_edge += bob_set.union(v1, v2)
        if (alice_set.is_complete()) & (bob_set.is_complete()):
            return len(edges) - num_edge
        return -1


class DisjoinSet:
    def __init__(self, n):
        self.component_size = n
        self.components = [1 for _ in range(n + 1)]
        self.rep = [i for i in range(n + 1)]

    def find_represent(self, v):
        if self.rep[v] == v:
            return v
        self.rep[v] = self.find_represent(self.rep[v])
        return self.rep[v]

    def union(self, v1, v2):
        v1_rep, v2_rep = self.find_represent(v1), self.find_represent(v2)
        if v1_rep == v2_rep:
            return 0
        else:
            if self.components[v1_rep] > self.components[v2_rep]:
                self.components[v1_rep] += self.components[v2_rep]
                self.rep[v2_rep] = v1_rep
            else:
                self.components[v2_rep] += self.components[v1_rep]
                self.rep[v1_rep] = v2_rep
            self.component_size -= 1
            return 1

    def is_complete(self):
        return self.component_size == 1


solution = Solution()
print(
    solution.maxNumEdgesToRemove(
        4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    )
)
