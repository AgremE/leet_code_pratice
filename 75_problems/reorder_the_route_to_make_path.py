from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        direct = {}
        reversed = {}
        for a, b in connections:
            if a in direct:
                direct[a].add(b)
            else:
                direct[a] = set(b)
            if b in reversed:
                reversed[b].add(a)
            else:
                reversed[b] = set(a)
