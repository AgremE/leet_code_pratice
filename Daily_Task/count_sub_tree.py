from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def construct_tree(edges):
            tree = {}
            for edge in edges:
                if edge[0] in tree:
                    tree[edge[0]].append(edge[1])
                else:
                    tree[edge[0]] = [edge[1]]
            return tree

        _tree = construct_tree(edges)

        def traverse_tree(_node, _tree, _ind, labels, ls_subtree):
            sub_tree = [labels[_ind]]
            sub_tree_node = []
            ### loop to traverse all the node in subtree
            for nd in _node:
                if nd in _tree:
                    temp_node = traverse_tree(_tree[nd], _tree, nd, labels, ls_subtree)
                    ls_subtree[nd] = temp_node
                    sub_tree_node = sub_tree_node + temp_node
                else:
                    ls_subtree[nd] = [labels[nd]]
                    sub_tree_node = sub_tree_node + [labels[nd]]
            sub_tree = sub_tree + sub_tree_node
            ls_subtree[_ind] = sub_tree
            return sub_tree

        ls_subtree = [0 for i in range(n)]
        overall_count = traverse_tree(_tree[0], _tree, 0, labels, ls_subtree=ls_subtree)
        result = []
        for ind in range(len(ls_subtree)):
            vertext = ls_subtree[ind]
            if vertext == 0:
                result.append(0)
            else:
                init_v = labels[ind]
                count = 0
                for _next_v in vertext:
                    if init_v == _next_v:
                        count = count + 1
                result.append(count)
        return result


solution = Solution()
print(solution.countSubTrees(n=4, edges=[[0, 2], [0, 3], [1, 2]], labels="aeed"))
