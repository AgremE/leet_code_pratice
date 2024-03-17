class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def get_tree(edges):
            tree = {}
            for v1, v2 in edges:
                if v1 in tree:
                    tree[v1].append(v2)
                else:
                    tree[v1] = [v2]
                if v2 in tree:
                    tree[v2].append(v1)
                else:
                    tree[v2] = [v1]
            return tree

        _tree = get_tree(edges)
        have_apple_node = [0 for i in range(n)]

        def dfs(_tree, root_node=0, already_visit=set()):
            if root_node in already_visit:
                return [hasApple[root_node]]
            sub_node = _tree[root_node]
            subtree_node_apple = [hasApple[root_node]]
            already_visit.add(root_node)
            for _n in sub_node:
                if _n in already_visit:
                    continue
                temp_node = dfs(_tree, _n, already_visit)
                for _item in temp_node:
                    subtree_node_apple.append(_item)
            have_apple_node[root_node] = True if sum(subtree_node_apple) > 0 else False
            return subtree_node_apple

        dfs(_tree, 0, [])
        total_walk = [1 if x else 0 for x in have_apple_node]
        total_v = sum(total_walk)
        if total_v == 0:
            return 0
        return (total_v - 1) * 2
