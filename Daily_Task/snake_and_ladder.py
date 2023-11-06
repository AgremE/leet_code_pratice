from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_coor_from_ind(ind, n):
            x = n - (ind // n + 1)
            y = (ind - 1) % n
            return x, y

        def get_graph(board):
            n = len(board)
            graph = {}
            for i in range(1, n**2 + 1):
                x, y = get_coor_from_ind(i, n)
                _input = board[x][y]
                if _input == -1:
                    graph[i] = [x for x in range(i + 1, min(i + 7, n**2 + 1))]
                else:
                    graph[i] = [_input]
            return graph

        def bfs(graph, start, target):
            next_vertex = graph[start]
            already_visited = [start]
            cost = {start: 0}
            step = 0
            next_step_vertext = []
            while next_vertex:
                n_v = next_vertex.pop()
                if n_v in already_visited:
                    continue
                already_visited.append(n_v)
                x, y = get_coor_from_ind(n_v, len(board))
                if board[x][y] == -1:
                    cost[n_v] = step + 1
                    next_step_vertext = graph[n_v] + next_step_vertext
                else:
                    cost[n_v] = step + 1
                    cost[graph[n_v][0]] = step + 1
                    already_visited.append(n_v)
                    already_visited.append(graph[n_v][0])
                    next_step_vertext = graph[graph[n_v][0]] + next_step_vertext
                if not next_vertex:
                    next_vertex = [
                        x for x in next_step_vertext if x not in already_visited
                    ]
                    next_vertex = list(set(next_vertex))
                    next_vertex.sort()
                    next_step_vertext = []
                    step = step + 1
            return cost

        n = len(board)
        print(get_graph(board))
        cost = bfs(get_graph(board), 1, n**2)
        print(cost)
        if n**2 not in cost:
            return -1
        return cost[n**2]


solution = Solution()
print(solution.snakesAndLadders(board=[[-1, 4, -1], [6, 2, 6], [-1, 3, -1]]))
