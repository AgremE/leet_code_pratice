from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return True
        first_cor = coordinates[0]
        second_cor = coordinates[1]
        a = (first_cor[0] - second_cor[0]) / (first_cor[1] - second_cor[1])
        b = first_cor[0] - a * first_cor[1]
        for coor in coordinates:
            if coor[0] != a * coor[1] + b:
                return False
        return True


solution = Solution()
print(solution.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
