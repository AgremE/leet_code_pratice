from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = 0
        if low < root.val and root.val < high:
            result = sum(
                [
                    root.val,
                    self.rangeSumBST(root.left, low, high),
                    self.rangeSumBST(root.right, low, high),
                ]
            )
        elif root.val <= low:
            value_add = root.val if root.val == low else 0
            result = sum([value_add, self.rangeSumBST(root.right, low, high)])
        elif root.val >= high:
            value_add = root.val if root.val == high else 0
            result = sum([value_add, self.rangeSumBST(root.left, low, high)])
        return result


root = TreeNode()
root.val = 10
root.left = TreeNode(val=5)
root.right = TreeNode(val=15)
root.left.left = TreeNode(val=3)
root.left.right = TreeNode(val=7)
root.right.right = TreeNode(val=18)

solution = Solution()
print(solution.rangeSumBST(root, low=7, high=15))
