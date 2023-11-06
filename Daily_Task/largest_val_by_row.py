from typing import List, Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue_cur = [root]
        queue_next = []
        if root is None:
            return []
        result = []
        temp_max_lvl = -math.inf
        while queue_cur:
            cur_node = queue_cur.pop()
            queue_next.append(cur_node.left)
            queue_next.append(cur_node.right)
            if temp_max_lvl < cur_node.val:
                temp_max_lvl = cur_node.val
            if queue_cur == []:
                queue_cur = queue_next
                queue_next = []
                result.append(temp_max_lvl)
                temp_max_lvl = -math.inf
        return result


solution = Solution()
print(solution.largestValues())
