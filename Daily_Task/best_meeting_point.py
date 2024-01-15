from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Let bruce force this in both axis x and y

        def get_one_row_col(grid):
            row_one = []
            col_one = []
            for i_row in range(len(grid)):
                for j_col in range(len(grid[0])):
                    if grid[i_row][j_col] == 1:
                        row_one.append(i_row)
                        col_one.append(j_col)
            return row_one, col_one

        def get_min_sum(loc_list, max_pos):
            return min(
                [sum([abs(pos - x) for x in loc_list]) for pos in range(max_pos)]
            )

        # min along x
        max_row = len(grid)

        # min along y
        max_col = len(grid[0])
        row_one, col_one = get_one_row_col(grid=grid)
        return get_min_sum(row_one, max_pos=max_row) + get_min_sum(
            col_one, max_pos=max_col
        )


solution = Solution()
print(solution.minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
print(solution.minTotalDistance([[1, 1]]))
