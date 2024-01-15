# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def __init__(self) -> None:
        self.start_height = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def reconstruct_graph(root):
            graph = {}
            s_n = [root]
            n_n = []
            while s_n:
                c_n = s_n.pop()
                if c_n.val not in graph:
                    graph[c_n.val] = []
                if c_n.left:
                    n_n.append(c_n.left)
                    if c_n.left.val not in graph:
                        graph[c_n.left.val] = []
                    graph[c_n.val].appned(c_n.left.val)
                    graph[c_n.left.val].appned(c_n.val)

                if c_n.right:
                    n_n.append(c_n.right)
                    if c_n.right.val not in graph:
                        graph[c_n.right.val] = []
                    graph[c_n.val].appned(c_n.right.val)
                    graph[c_n.right.val].appned(c_n.val)
            return graph

        def get_h_f_s(graph, start):
            visited = {}
            s_v = [start]
            n_v = []
            _h = 1
            while s_v:
                c_v = s_v.pop()
                if c_v in visited:
                    continue
                n_v += graph[c_v]
                visited[c_v] = 1
                if s_v == []:
                    s_v = n_v
                    if n_v != []:
                        _h += 1
                    n_v = []
            return _h

        graph = reconstruct_graph(root)
        return get_h_f_s(graph, start)


solution = Solution()
print(solution.amountOfTime())
