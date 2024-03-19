from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        reversed = {}
        reverse_root = []
        for a, b in connections:
            if b == 0:
                reverse_root.append(a)
            if a in reversed:
                reversed[a].add(b)
            else:
                reversed[a] = set([b])
        count = 0
        temp_start_v = set()
        tracker = set()
        for v in reverse_root:
            tracker.add(v)
        if 0 in reversed:
            start_v = reversed[0]
        start_v += reverse_root
        while start_v:
            _v = start_v.pop()
            if _v in reversed:
                temp_start_v.union(reversed[_v])
            if not start_v:
                start_v = list(temp_start_v)
            if _v in tracker:
                continue
            tracker.add(_v)
            count += 1
        return count
