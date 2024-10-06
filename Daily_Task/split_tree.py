# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:

        if root.val >= target:
            if root.left and root.left.val >= target:
                return self.splitBST(root.left, target)
            else:
                left = root.left
                root.left = None
                return left, root
        else:
            if root.right and root.right.val <= target:
                return self.splitBST(root.right, target)
            else:
                right = root.right
                root.right = None
                return root, right
