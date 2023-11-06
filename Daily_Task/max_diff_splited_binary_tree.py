# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.memoir_store = {}

    def store_agg_each_node(self, root, start_index=0):
        left_index = 2 * start_index + 1
        right_index = 2 * start_index + 2
        if start_index in self.memoir_store:
            return self.memoir_store[start_index]
        if not root.left and not root.right:
            self.memoir_store[start_index] = root.val
        if root.left and root.right:
            self.memoir_store[start_index] = (
                root.val
                + self.store_agg_each_node(root.left, left_index)
                + self.store_agg_each_node(root.right, right_index)
            )
        elif root.left:
            self.memoir_store[start_index] = root.val + self.store_agg_each_node(
                root.left, left_index
            )
        elif root.right:
            self.memoir_store[start_index] = root.val + self.store_agg_each_node(
                root.right, right_index
            )
        return self.memoir_store[start_index]

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.store_agg_each_node(root, start_index=0)
        store_sum = []
        for ind, val in self.memoir_store.items():
            store_sum.append(val)
        max_val = max(store_sum)
        if len(store_sum) == 1:
            return max_val
        reminding = [max_val - x for x in store_sum]
        result_max = [x[0] * x[1] for x in zip(store_sum, reminding)]
        result_max_modulo = max(result_max) % (10**9 + 7)
        return result_max_modulo


solution = Solution()
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
print(solution.maxProduct(root))
