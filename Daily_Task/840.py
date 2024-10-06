from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def getsubgrid(x1, y1, x2, y2, _grid):
            return [item[x1:x2] for item in _grid[y1:y2]]

        def _verfied(_grid):
            _each_sum = set([])
            _all_num = set([])
            for row in _grid:
                for num in row:
                    _all_num.add(num)
            if len(_all_num) != 9:
                return False
            else:
                for i in range(1, 10):
                    if i not in _all_num:
                        return False
            for row in _grid:
                _each_sum.add(sum(row))
            for col in range(3):
                _each_sum.add(sum([row[col] for row in _grid]))
            _each_sum.add(_grid[0][0] + _grid[1][1] + _grid[2][2])
            _each_sum.add(_grid[2][0] + _grid[1][1] + _grid[0][2])
            if len(_each_sum) == 1:
                return True
            return False

        count = 0
        for row in range(3, len(grid) + 1):
            for col in range(3, len(grid[0]) + 1):
                _grid = getsubgrid(row - 3, col - 3, row, col, grid)
                if _verfied(_grid):
                    count += 1
        return count


solution = Solution()
print(solution.numMagicSquaresInside(grid=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
