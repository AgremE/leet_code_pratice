# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ##
        # Description of the algorithm
        # First, construct an adj matrix that represent the graph from a tree
        # As the value of the node under 500, just used the index of adj matrix
        # as an indicatore value, this allowed us to find the diameter coverage of
        # all the node value that we see
        #
        # The above way of thinking is not correct because double way of travelling
        # I believe that the brust way forward is the reconstruct the tree using
        # target node as root.
        # #
        _matrix = [[-1 for x in range(501)] for y in range(501)]

        def construc_matrix(root: TreeNode, matrix: List[List[int]]):
            if not root:
                return matrix
            val = root.val
            if root.left:
                matrix[val][root.left.val] = 2
                matrix[root.left.val][val] = 2
                construc_matrix(root.left, matrix)
            if root.right:
                matrix[val][root.right.val] = 2
                matrix[root.right.val][val] = 2
                construc_matrix(root.right, matrix)
            return matrix

        _matrix = construc_matrix(root, _matrix)
        ### Get the diametter from target node
        init_list = [i for i, x in enumerate(_matrix[target.val]) if x == 2]
        for i_k in range(k - 1):
            temp_list = []
            while init_list:
                node_val = init_list.pop()
                temp_list.extend([i for i, x in enumerate(_matrix[node_val]) if x == 2])
            init_list = list(set(temp_list))
            init_list = [x for x in init_list if x != target.val]
        return init_list


# root = TreeNode(x=3)

# root.left = TreeNode(x=5)
# root.right = TreeNode(x=1)

# root.left.left = TreeNode(x=6)
# root.left.right = TreeNode(x=2)

# root.right.left = TreeNode(x=0)
# root.right.right = TreeNode(x=8)

# root.left.right.left = TreeNode(x=7)
# root.left.right.right = TreeNode(x=4)

root = TreeNode(x=0)

root.left = TreeNode(x=1)
root.right = TreeNode(x=3)

root.left.right = TreeNode(x=2)

solution = Solution()
print(solution.distanceK(root, target=TreeNode(x=1), k=2))
