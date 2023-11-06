from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root: TreeNode, count_dict={}):
            if root.val in count_dict:
                count_dict[root.val] += 1
            else:
                count_dict[root.val] = 1
            traverse_list = []
            branch_list = []
            if root.left:
                traverse_list.append(root.left)
            if root.right:
                traverse_list.append(root.right)
            while traverse_list:
                node_extr = traverse_list.pop()
                if node_extr.val in count_dict:
                    count_dict[node_extr.val] += 1
                else:
                    count_dict[node_extr.val] = 1
                if node_extr.left:
                    branch_list.append(node_extr.left)
                if node_extr.right:
                    branch_list.append(node_extr.right)
                if not traverse_list:
                    traverse_list = branch_list
                    branch_list = []
            _max_count = 0
            _mode = 0
            for i, _count in traverse_list.items():
                if _count > max_count:
                    max_count = _count
                    _mode = i
            return _mode

        return traverse(root)
