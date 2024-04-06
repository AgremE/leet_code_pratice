from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.count = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, cur_sum, targetsum):
            cur_sum = cur_sum + root.val
            if cur_sum == targetSum:
                self.count += 1
            if root.left:
                dfs(root.left, cur_sum, targetsum)
            if root.right:
                dfs(root.right, cur_sum, targetsum)

        next_v = [root]
        temp_next_v = []
        while next_v:
            _n = next_v.pop()
            dfs(_n, 0, targetSum)
            if _n.left:
                temp_next_v.append(_n.left)
            if _n.right:
                temp_next_v.append(_n.right)
            if not next_v:
                next_v = temp_next_v


root = TreeNode()
