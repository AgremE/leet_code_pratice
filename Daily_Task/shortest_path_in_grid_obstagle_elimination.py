from typing import List


class Solution:
    def get_min_step_neg(self, max_x, position):
        possible_position = []
        if position[0] - 1 >= 0:
            possible_position.append([position[0] - 1, position[1]])  ### Left neg
        if position[1] - 1 >= 0:
            possible_position.append([position[0], position[1] - 1])  ### Top neg
        if position[0] + 1 < max_x:
            possible_position.append([position[0] + 1, position[1]])  ### Right neg
        return possible_position

    def get_cost(pos, grid):
        if grid[pos[0]][pos[1]] == 1:
            return 10**5
        else:
            return 1

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        y_dir = len(grid)
        x_dir = len(grid[0])
        tracker = [[10**5 for _ in range(y_dir)] for _ in range(x_dir)]
        tracker[0][0] = 1
        for y in range(y_dir):
            for i in range(2):
                for x in range(x_dir):
                    possible_positions = self.get_min_step_neg(x_dir, [x, y])
                    temp_min = []
                    for pos in possible_positions:
                        temp_min.append(
                            tracker[pos[0]][pos[1]] + self.get_cost(pos, grid)
                        )
                    min_weight = min(temp_min)
                    tracker[x, y] = min_weight
        return tracker


solution = Solution()
print(
    solution.shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1)
)
