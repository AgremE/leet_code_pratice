from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_min_max(node, f_min_val=10**5 + 10, s_min_val=10**5 + 10):
            if not node:
                return f_min_val, s_min_val
            val = node.val
            if val < f_min_val:
                s_min_val = f_min_val
                f_min_val = val
            elif val < s_min_val:
                s_min_val = val
            f_min_left, s_min_left = get_min_max(node.left, f_min_val, s_min_val)
            f_min_right, s_min_right = get_min_max(node.right, f_min_val, s_min_val)
            f_min = min(f_min_val, f_min_left, f_min_right)
            s_min = min(s_min_val, s_min_left, s_min_right)
            return f_min, s_min

        f_min, s_min = get_min_max(root)
        return abs(f_min - s_min)


solution = Solution()
root = TreeNode()
root.val = 4
root.left = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(3))
root.right = TreeNode(val=6)
print(solution.getMinimumDifference(root))
