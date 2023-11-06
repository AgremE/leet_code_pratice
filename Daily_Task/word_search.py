from typing import List
from collections import deque


class Solution:
    def get_possible_move(self, cur_pos, max_x, max_y):
        x, y = cur_pos
        result = []
        if x - 1 >= 0:
            result.append([x - 1, y])
        if y - 1 >= 0:
            result.append([x, y - 1])
        if x + 1 < max_x:
            result.append([x + 1, y])
        if y + 1 < max_y:
            result.append([x, y + 1])
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        len_x = len(board)
        len_y = len(board[0])
        for x in range(len_x):
            for y in range(len_y):
                elem = board[x][y]
                if elem == word[0]:
                    ## start searching from here
                    stack = deque()
                    already_visit = {}
                    already_visit[100 + x * 10 + y] = 1
                    stack.append([x, y, 0, already_visit])
                    while stack:
                        x, y, score, already_visit = stack.pop()
                        _already_visit = already_visit.copy()
                        if score == len(word) - 1:
                            return True
                        possible_move = self.get_possible_move([x, y], len_x, len_y)
                        for _move in possible_move:
                            _mv_x, _mv_y = _move
                            tracker = 100 + _mv_x * 10 + _mv_y
                            if tracker in _already_visit:
                                continue
                            else:
                                _already_visit[tracker] = 1
                                _elem = board[_mv_x][_mv_y]
                                if _elem == word[score + 1]:
                                    stack.append(
                                        [_mv_x, _mv_y, score + 1, _already_visit]
                                    )
                else:
                    continue
        return False


solution = Solution()

print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)


print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)

print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
)

print(
    solution.exist(
        board=[["a", "b"]],
        word="ba",
    )
)
