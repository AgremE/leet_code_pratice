from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col] == 1:
                    for l_row in range(row, len(land)):
                        if land[l_row][col] == 0:
                            break
                        for l_col in range(col, len(land[0])):
                            if land[l_row][l_col]:
                                land[l_row][l_col] = 0
                            else:
                                break
                    result.append([row, col, l_row - 1, l_col - 1])
        return result
