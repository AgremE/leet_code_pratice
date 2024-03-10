# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        n_v = deque([root])
        temp_n_v = deque([])
        lvl_value = []
        lvl = 0
        while n_v:
            _n = n_v.popleft()
            if _n.left:
                temp_n_v.append(_n.left)
            if _n.right:
                temp_n_v.append(_n.right)
            lvl_value.append(_n.val)
            if not n_v:
                if lvl%2==1:
                    for i in range(1,len(lvl_value)):
                        if lvl_value[i-1] - lvl_value[i] > 0:
                            return False
                else:
                    for i in range(1,len(lvl_value)):
                        if lvl_value[i] - lvl_value[i-1] < 0:
                            return False
                lvl+=1
                n_v = temp_n_v
                temp_n_v = deque([])
                lvl_value = []
        return True
