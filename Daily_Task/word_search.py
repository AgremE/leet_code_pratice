from typing import List


class Solution:
    def __init__(self) -> None:
        self.found = False

    def get_possible_mov(self, i, j, m, n):
        result = [[i, j + 1], [i, j - 1], [i - 1, j], [i + 1, j]]
        return [
            x
            for x in result
            if (x[0] >= 0) and (x[0] < m) and (x[1] >= 0) and (x[1] < n)
        ]

    def dfs(self, _mov, _c_i, board, word, visited):
        if _c_i == len(word):
            self.found = True
            return True
        if tuple(_mov) in visited:
            return None
        if board[_mov[0]][_mov[1]] == word[_c_i]:
            visited.add(tuple(_mov))
            pos_movs = self.get_possible_mov(
                _mov[0], _mov[1], len(board), len(board[0])
            )
            for _n_m in pos_movs:
                self.dfs(_n_m, _c_i + 1, board, word, visited)
            visited.remove(tuple(_mov))
            if len(word) == 1:
                self.found = True

    def exist(self, board: List[List[str]], word: str) -> bool:
        graph = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                _c_i = 0
                self.dfs((i, j), _c_i, board, word, visited)
        return self.found


solution = Solution()

# print(
#     solution.exist(
#         board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
#         word="ABCCED",
#     )
# )


print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        word="ABCESEEEFS",
    )
)

# print(
#     solution.exist(
#         board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
#         word="SEE",
#     )
# )

# print(
#     solution.exist(
#         board=[["a", "b"]],
#         word="ba",
#     )
# )
