from typing import Optional

# def recur(root, node_index, arr):
#                 if not root:
#                     return arr
#                 arr[node_index] = root.right.val
#                 if root.left:
#                     arr = recur(root.left, node_index * 2, arr)
#                 if root.right:
#                     arr = recur(root.right, node_index * 2 + 1, arr)
#                 return arr

#             def get_sub_total(ind,memoir,arr,child_node):
#                 if ind in memoir:
#                     return memoir[ind]
#                 if ind in child_node:
#                     return
#                 if (ind*2<1001) and (ind*2+1<1001):
#                     memoir[ind] = get_sub_total(ind*2,memoir,arr,child_node)+get_sub_total(ind*2+1,memoir,arr,child_node)
#                 else:
#                     memoir[ind] = 0
#                 return memoir

#             arr = recur(root, 1, arr)
#             arr = arr[::-1]
#             sub_total = [0 _ in range(1001)]
#             sub_count = [0 for _ in range(1001)]

#             for i in range(len(arr)):
#                 sub_total[i] = arr[2*i] + arr[i*2+1] + sub_total[2*i] + sub_total[2*i+1]
#                 sub_count[i] = sub_count[2*i] + sub_count[2*i+1] + 2


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def recur(root, node_ind, memior, each_node):
            if node_ind not in each_node:
                each_node[node_ind] = root.val
            if not root:
                return 0
            if node_ind in memior:
                return memior[node_ind]
            if not root.left and not root.right and root.val != None:
                memior[node_ind] = 0
                return memior[node_ind]
            if root.left and not root.right:
                memior[node_ind] = root.left.val + recur(
                    root.left, node_ind * 2, memior, each_node
                )
            if root.right and not root.left:
                memior[node_ind] = root.right.val + recur(
                    root.right, node_ind * 2 + 1, memior, each_node
                )
            if root.right and root.left:
                memior[node_ind] = (
                    root.left.val
                    + recur(root.left, node_ind * 2, memior, each_node)
                    + root.right.val
                    + recur(root.right, node_ind * 2 + 1, memior, each_node)
                )
            return memior[node_ind]

        def recur_count(root, node_ind, memior):
            if not root:
                return 0
            if node_ind in memior:
                return memior[node_ind]
            if not root.left and not root.right:
                memior[node_ind] = 0
                return memior[node_ind]
            if root.left and not root.right:
                memior[node_ind] = 1 + recur_count(root.left, node_ind * 2, memior)
            if root.right and not root.left:
                memior[node_ind] = 1 + recur_count(root.right, node_ind * 2 + 1, memior)
            if root.right and root.left:
                memior[node_ind] = (
                    2
                    + recur_count(root.left, node_ind * 2, memior)
                    + recur_count(root.right, node_ind * 2 + 1, memior)
                )
            return memior[node_ind]

        memior_total_sum = {}
        memior_total_count = {}
        each_node = {}
        total_sum = recur(root, 1, memior=memior_total_sum, each_node=each_node)
        total_count = recur_count(root, 1, memior=memior_total_count)
        count_same_avg = 0
        for node_id, sub_sum in memior_total_sum.items():
            _avg_check = sub_sum + each_node[node_id]
            _avg_check = (_avg_check) / (memior_total_count[node_id] + 1)
            if (each_node[node_id]) == int(_avg_check):
                count_same_avg += 1
        return count_same_avg


root = TreeNode(val=4)
root.left = TreeNode(val=8)
root.right = TreeNode(val=5)

root.left.left = TreeNode(val=0)
root.left.right = TreeNode(val=1)

root.right.right = TreeNode(val=6)

solution = Solution()
print(solution.averageOfSubtree(root))
