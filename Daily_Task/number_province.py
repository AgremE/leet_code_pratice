from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def get_connect(isConnected):
            result = {}
            for i in range(len(isConnected)):
                conn = isConnected[i]
                for j in range(len(conn)):
                    if (conn[j] == 0) or (i == j):
                        continue
                    if (i, j) in result or (j, i) in result:
                        continue
                    result[(i, j)] = 1
            return list(result.keys())

        unique_conn = get_connect(isConnected)
        roots = [i for i in range(len(isConnected))]

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

        for conn in unique_conn:
            roots = union(conn[0], conn[1], roots)
        return sum([1 if x == roots[x] else 0 for x in range(len(roots))])


solution = Solution()
print(solution.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution.findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
