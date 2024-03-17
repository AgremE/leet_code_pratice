from typing import List


class Solution:
    def search_space(self, v_pos, grid, memoir, already_visit={}):

        if len(grid) - 1 == v_pos[0] and len(grid[0]) - 1 == v_pos[1]:
            return 1
        if (
            len(grid) <= v_pos[0]
            or len(grid[0]) <= v_pos[1]
            or v_pos[0] < 0
            or v_pos[1] < 0
            or grid[v_pos[0]][v_pos[1]] == 1
            or f"{v_pos[0]}_{v_pos[1]}" in already_visit
        ):
            return 10**5
        already_visit[f"{v_pos[0]}_{v_pos[1]}"] = 1
        go_up = v_pos[0] - 1, v_pos[1]
        go_down = v_pos[0] + 1, v_pos[1]
        go_left = v_pos[0], v_pos[1] - 1
        go_right = v_pos[0], v_pos[1] + 1
        go_up_left = v_pos[0] - 1, v_pos[1] - 1
        go_up_right = v_pos[0] - 1, v_pos[1] + 1
        go_down_left = v_pos[0] + 1, v_pos[1] - 1
        go_down_right = v_pos[0] + 1, v_pos[1] + 1
        return min(
            1 + self.search_space(go_up, grid, memoir),
            1 + self.search_space(go_down, grid, memoir),
            1 + self.search_space(go_left, grid, memoir),
            1 + self.search_space(go_right, grid, memoir),
            1 + self.search_space(go_up_left, grid, memoir),
            1 + self.search_space(go_up_right, grid, memoir),
            1 + self.search_space(go_down_left, grid, memoir),
            1 + self.search_space(go_down_right, grid, memoir),
        )

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        s_v = grid[0][0]
        e_v = grid[0][0]
        if s_v == 1 or e_v == 1:
            return -1
        ### agent can  visit 8 direction
        memoir = []
        result = self.search_space([0, 0], grid, memoir)
        if result >= 10**5:
            return -1
        return result


test = Solution()
print(test.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(test.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
