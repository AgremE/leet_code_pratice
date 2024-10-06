# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Use post order search to find count he distance from LCS of current node (Regarding the current node as LCS of all the leaf node)
        """

        def post_order(root, distance):
            current = [0 for _ in range(11)]
            if not root:
                return current
            if root.left == None and root.right == None:
                current[0] = 1  
                return current
            _left_distance = post_order(root.left, distance)
            _right_distance = post_order(root.right, distance)
            for i in range(10):
                current[i + 1] += _left_distance[i] + _right_distance[i]

            for d_i in range(distance):
                for d_j in range(distance):
                    if 2 + d_i + d_j <= distance:
                        current[11] += _right_distance[d_i] + _left_distance[d_j]
            return current
