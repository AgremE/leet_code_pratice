from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ### validate rows
        rows = [row for row in board]
        for row in rows:
            count = {}
            for num in row:
                if num != ".":
                    if num in count:
                        return False
                    else:
                        count[num] = 1
        ### validate columns
        columns = list(zip(*board))
        for col in columns:
            count = {}
            for num in col:
                if num != ".":
                    if num in count:
                        return False
                    else:
                        count[num] = 1
        ### validate gride
        start_index_list = [0, 3, 6]
        list_result = []
        for row_add in [0, 3, 6]:
            list_result.append(
                [
                    [
                        board[i][row_add : row_add + 3]
                        for i in range(start_index, start_index + 3)
                    ]
                    for start_index in start_index_list
                ]
            )
        for list_gride in list_result:
            for gride in list_gride:
                count = {}
                for list_num in gride:
                    for num in list_num:
                        if num != ".":
                            if num in count:
                                return False
                            else:
                                count[num] = 1
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solution = Solution()
print(solution.isValidSudoku(board))
board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(solution.isValidSudoku(board))
