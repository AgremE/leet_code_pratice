# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        most_left = root.val
        next_q = deque()
        assing = False
        while q:
            n = q.popleft()
            if n.left:
                if not assing:
                    most_left = n.left.val
                    assing = True
                next_q.append(n.left)
            if n.right:
                next_q.append(n.left)
            if not q:
                q = next_q.copy()
                next_q = deque()
                assing = False
        return most_left
