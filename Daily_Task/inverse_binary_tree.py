from typing import Optional
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        if (not root.left) and (not root.right):
            return root
        left_node = copy.copy(root.left)
        right_node = copy.copy(root.right)
        if right_node:
            root.left = self.invertTree(right_node)
        else:
            root.left = right_node
        if left_node:
            root.right = self.invertTree(left_node)
        else:
            root.right = left_node
        return root


# [4,2,7,1,3,6,9]
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)
root = TreeNode(1)
root.left = TreeNode(2)

solution = Solution()
print(solution.invertTree(root))
print("test")
