# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Correct answer but not efficient
class Solution(object):
    def __init__(self):
        self.count = 0

    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def get_sum(node, i, memoir, node_value):
            if i in memoir:
                return memoir[i] + node_value[i]
            if not node:
                return 0
            if (not node.left) and (not node.right):
                memoir[i] = node.val
                if node.val == 0:
                    self.count += 1
                return memoir[i]
            elif not node.left:
                node_value[i] = node.val
                memoir[i] = get_sum(node.right, i * 2, memoir, node_value)
            elif not node.right:
                node_value[i] = node.val
                memoir[i] = get_sum(node.left, i * 2 + 1, memoir, node_value)
            else:
                node_value[i] = node.val
                memoir[i] = get_sum(node.left, i * 2, memoir, node_value) + get_sum(
                    node.right, i * 2 + 1, memoir, node_value
                )
            return memoir[i] + node_value[i]

        memior = {}
        node_value = {}
        get_sum(root, 1, memior, node_value)
        for node, value in node_value.items():
            if memior[node] == value:
                self.count += 1
        return self.count


# Decently good solution
from collections import deque


class Solution(object):
    def __init__(self):
        self.count = 0

    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def get_sum(node):
            if not node:
                return 0
            left = get_sum(node.left)
            right = get_sum(node.right)
            if node.val == (left + right):
                self.count += 1
            return left + right + node.val

        get_sum(root)
        return self.count


root = TreeNode(10)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)

solution = Solution()
print(solution.equalToDescendants(root))
