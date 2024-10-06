from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cluster_tracker = {}
        cluster = {}

        def return_connection(grid, row, col):
            result = []
            if row - 1 >= 0:
                if grid[row - 1][col] == "1":
                    result.append((row - 1, col))
            if col - 1 >= 0:
                if grid[row][col - 1] == "1":
                    result.append((row, col - 1))
            return result

        next_cluster = 1
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    connetion = return_connection(grid, row, col)
                    if len(connetion) == 1:
                        connetion = connetion[0]
                        if (connetion[0], connetion[1]) in cluster_tracker:
                            cluster_num = cluster_tracker[(connetion[0], connetion[1])]
                            cluster_tracker[(row, col)] = cluster_num
                            cluster[cluster_num].add((row, col))
                        else:
                            cluster_num = next_cluster
                            next_cluster += 1
                            cluster_tracker[(row, col)] = cluster_num
                            cluster[cluster_num] = set([(row, col)])
                    elif len(connetion) == 0:
                        cluster[next_cluster] = set([(row, col)])
                        cluster_tracker[(row, col)] = next_cluster
                        next_cluster += 1
                    else:
                        conn1, conn2 = connetion
                        compo1 = cluster_tracker[(conn1[0], conn1[1])]
                        compo2 = cluster_tracker[(conn2[0], conn2[1])]
                        if compo1 == compo2:
                            cluster_tracker[(row, col)] = compo1
                            cluster[compo1].add((row, col))
                        else:
                            compo2_elem = cluster[compo2]
                            for elem in compo2_elem:
                                cluster_tracker[elem] = compo1
                            cluster[compo1] = cluster[compo1].add(cluster[compo2])
                            del cluster[compo2]
                            cluster_tracker[(row, col)] = compo1
                            cluster[compo1].add((row, col))
        return len(cluster)


solution = Solution()
print(
    solution.numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
