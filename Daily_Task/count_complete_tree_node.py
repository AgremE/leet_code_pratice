from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        already_visit = []
        will_visit = []
        if root == None:
            return 0
        already_visit.append(root)
        if root.left:
            will_visit.append(root.left)
        if root.right:
            will_visit.append(root.right)
        while will_visit:
            node = will_visit.pop()
            if node.left:
                will_visit.append(node.left)
            if node.right:
                will_visit.append(node.right)
            already_visit.append(node)
        return len(already_visit)


root = TreeNode()
# root.left = TreeNode(5)
# root.right = TreeNode(5)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(5)

solution = Solution()
print(solution.countNodes(root))
