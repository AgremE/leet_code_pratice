
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.max_path = -1
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_path = 0
        def recurv(root,last_turn,count):
            self.max_path = max(self.max_path,count)
            if not root:
                return
            if last_turn == 0:
                if root.left:
                    recurv(root.left,last_turn=1,count=1)
                if root.right:
                    recurv(root.right,last_turn=2,count=1)
            if last_turn == 1:
                if root.right:
                    recurv(root.right,last_turn=2,count=count+1)
                if root.left:
                    recurv(root.left,last_turn=1,count=1)
            if last_turn == 2:
                if root.left:
                    recurv(root.left,last_turn=1,count=count+1)
                if root.right:
                    recurv(root.right,last_turn=2,count=1)

        recurv(root,last_turn=0,count=1)
        return self.max_path