from typing import List
from collections import Counter


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        def traverse_tree(node, list_left, list_right, current_visit=[]):
            if node == -1:
                return current_visit
            if len(current_visit) == n:
                return current_visit
            if node in current_visit:
                return current_visit
            current_visit.append(node)
            current_visit = traverse_tree(
                list_left[node], list_left, list_right, current_visit=current_visit
            ) + traverse_tree(
                list_right[node], list_left, list_right, current_visit=current_visit
            )
            return list(set(current_visit))

        def valide_tree(number_vertex, number_edge, in_degree, out_degree):

            if number_edge != number_vertex - 1:
                return False
            for i in range(len(in_degree)):
                i_d = in_degree[i]
                if i_d == 0:
                    list_node = traverse_tree(i, leftChild, rightChild)
                    if len(list_node) != number_vertex:
                        return False
                if i_d > 1:
                    return False
            for out_d in out_degree:
                if out_d > 2:
                    return False
            # Count root node
            num_root = 0
            for i_d in in_degree:
                if i_d == 0:
                    num_root = num_root + 1
            if num_root > 1:
                return False
            return True

        number_edge = sum([1 if x > -1 else 0 for x in leftChild]) + sum(
            [1 if x > -1 else 0 for x in rightChild]
        )
        count_left_child = Counter(leftChild)
        count_right_child = Counter(rightChild)
        total_in_degree = [0 for _ in range(n)]
        # Get in degree
        for ind, value in count_left_child.items():
            if ind == -1:
                continue
            total_in_degree[ind] = total_in_degree[ind] + value

        for ind, value in count_right_child.items():
            if ind == -1:
                continue
            total_in_degree[ind] = total_in_degree[ind] + value

        out_degree_left = [1 if x > -1 else 0 for x in leftChild]
        out_degree_right = [1 if x > -1 else 0 for x in rightChild]
        total_out_degree = []
        for ind, (x, y) in enumerate(zip(out_degree_left, out_degree_right)):
            total_out_degree.append(x + y)
        return valide_tree(n, number_edge, total_in_degree, total_out_degree)


solution = Solution()
print(
    solution.validateBinaryTreeNodes(
        n=4, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1]
    )
)

print(
    solution.validateBinaryTreeNodes(
        n=4, leftChild=[1, 0, 3, -1], rightChild=[-1, -1, -1, -1]
    )
)
