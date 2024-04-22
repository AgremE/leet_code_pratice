# Definition for a binary tree node.
from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Let doing prefix sum on this problem wit bfs
        _min = math.inf
        n_v = [(root,0)]
        temp_n_v = []
        while n_v:
            v,pre_fix = n_v.pop()
            degree = max(math.ceil(math.log(pre_fix,10)),1) if pre_fix > 0 else 0
            if v.left:
                temp_n_v.append((v.left,(v.val+1)*10**degree+pre_fix))
            if v.right:
                temp_n_v.append((v.right,(v.val+1)*10**degree+pre_fix))
            if not (v.left) and (not v.right):
                curre_num = (v.val+1)*10**degree+pre_fix
                if _min>curre_num:
                    _min = curre_num
            if not n_v:
                n_v = temp_n_v
                temp_n_v = []
                if _min!=math.inf:
                    break
        result = []
        while _min:
            result.append(chr(ord('a')+(_min%10-1)))
            _min = _min //10
        return "".join(result)
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

solution = Solution()
print(solution.smallestFromLeaf(root))