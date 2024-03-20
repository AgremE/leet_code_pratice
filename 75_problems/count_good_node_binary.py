class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,cur_max,count=0):
            if cur_max<=root.val:
                count+=1
                cur_max = root.val
            if root.left:
                count += dfs(root.left,cur_max,0)
            if root.right:
                count+= dfs(root.right,cur_max,0)
            return count
        return dfs(root,root.val,0)