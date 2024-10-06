from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        Algorithm going as following:
        maintain the grid with island
        keep iterate to find the latest number of update cluster (Connected components), you can use the disjoin set for this one
        """
        cluster = {}
        tracker = {}
        grid = [[0 for _ in range(n)] for _ in range(m)]
        cur_cluster_id = 0

        def get_conneted_land(grid, pos):
            x, y = pos
            connected_node = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
            connected_node = [
                (x, y)
                for x, y in connected_node
                if (x >= 0 and x < m) and (y >= 0 and y < n)
            ]
            connected_node = [(x, y) for x, y in connected_node if grid[x][y] == "1"]
            return connected_node

        def update_cluster(cluster, tracker, grid, node, cur_cluster_id):
            connected_nodes = get_conneted_land(grid, node)
            node = (node[0], node[1])
            if node in tracker:
                return cluster, tracker, cur_cluster_id
            if not connected_nodes:
                cur_cluster_id += 1
                cluster[cur_cluster_id] = set([node])
                tracker[node] = cur_cluster_id
            else:
                merge_id = []
                for _node in connected_nodes:
                    merge_id.append(tracker[_node])
                _id = min(merge_id)
                for id in merge_id:
                    if id != _id:
                        nodes = cluster[id]
                        for _n in nodes:
                            tracker[_n] = _id
                        cluster[_id] = cluster[_id].union(cluster[id])
                for id in list(set(merge_id)):
                    if id != _id:
                        del cluster[id]
                cluster[_id].add(node)
                tracker[node] = _id
            return cluster, tracker, cur_cluster_id

        result = []
        for node in positions:
            grid[node[0]][node[1]] = "1"
            cluster, tracker, cur_cluster_id = update_cluster(
                cluster, tracker, grid, node, cur_cluster_id
            )
            result.append(len(cluster))
        return result


solution = Solution()
print(
    solution.numIslands2(
        3,
        3,
        [
            [0, 0],
            [0, 1],
            [1, 2],
            [2, 1],
            [1, 0],
            [0, 0],
            [2, 2],
            [1, 2],
            [1, 1],
            [0, 1],
        ],
    )
)
