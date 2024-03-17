from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leave_node(root):
            result = []
            # this is bread first search but we should use deep first search
            # visited = deque()
            # visited.append(root)
            # if root is None:
            #     return result
            # while visited:
            #     node = visited.popleft()
            #     left_node = node.left
            #     right_node = node.right
            #     if left_node is None and right_node is None:
            #         result.append(node.val)
            #     if left_node:
            #         visited.append(left_node)
            #     if right_node:
            #         visited.append(right_node)
            if not root:
                return []
            if root.left is None and root.right is None:
                result = result + [root.val]
            if root.left:
                result = result + get_leave_node(root.left)
            if root.right:
                result = result + get_leave_node(root.right)
            return result

        root1_leave = get_leave_node(root1)
        root2_leave = get_leave_node(root2)
        len_root1 = len(root1_leave)
        len_root2 = len(root2_leave)
        if len_root1 != len_root2:
            return False
        for i in range(len(root1_leave)):
            if root1_leave[i] != root2_leave[i]:
                return False
        return True


root = TreeNode()
root.val = 3
root.left = TreeNode(val=5)
root.right = TreeNode(val=1)

root.left.left = TreeNode(val=6)
root.left.right = TreeNode(val=2)

root.right.left = TreeNode(val=9)
root.right.right = TreeNode(val=8)

root.left.right.left = TreeNode(val=7)
root.left.right.right = TreeNode(val=4)


root2 = TreeNode()
root2.val = 3
root2.left = TreeNode(val=5)
root2.right = TreeNode(val=1)
root2.left.left = TreeNode(val=6)
root2.left.right = TreeNode(val=7)

root2.right.left = TreeNode(val=4)
root2.right.right = TreeNode(val=2)

root2.right.right.left = TreeNode(val=9)
root2.right.right.right = TreeNode(val=8)

solution = Solution()
print(solution.leafSimilar(root, root2))
