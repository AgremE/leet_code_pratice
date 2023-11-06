from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs_possible_path(self, root, path=[], result=[]):
        if not root:
            return path
        path.append(root.val)
        if root.left is None and root.right is None:
            result.append(path.copy())
            path.pop()
            return path
        else:
            for child in [root.left, root.right]:
                self.dfs_possible_path(child, path, result)
            path.pop()
        return result

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ### Using DFS
        path_matrix = self.dfs_possible_path(root, path=[])
        max_result = 0
        for path in path_matrix:
            path_min = min(path)
            path_max = max(path)
            if abs(path_max - path_min) >= max_result:
                max_result = abs(path_max - path_min)
        return max_result


# root = TreeNode(8)
# root.left = TreeNode(3)
# root.right = TreeNode(10)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(6)
# root.right.right = TreeNode(14)
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(0)
root.right.right.left = TreeNode(3)

solution = Solution()
print(solution.maxAncestorDiff(root))
