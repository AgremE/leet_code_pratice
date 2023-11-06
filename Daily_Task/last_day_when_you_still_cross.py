from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def related_direction(x, y, max_x, max_y):
            all_direction = []
            if x < max_x:
                all_direction.append((x + 1, y))
            if x > 1:
                all_direction.append(x - 1, y)
            if y < max_y:
                all_direction.append((x, y + 1))
            if y > 1:
                all_direction.append((x, y - 1))
            return all_direction

        track_cluster = {}
        cluster_info = {}
        for cell in cells:
            x, y = cell
            possible_direction = related_direction(x, y, row, col)
            if (x, y) in track_cluster:
                pass
