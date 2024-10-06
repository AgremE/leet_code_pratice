from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.move = 0

        def dfs(root):
            if root == None:
                return 0
            left_coins = dfs(root.left)
            right_coins = dfs(root.right)
            self.move += abs(left_coins) + abs(right_coins)
            return (root.val - 1) + left_coins + right_coins

        dfs(root)
        return self.move
