class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0

        def q_coverage(board, pos):
            # queen cover the surroudning area and the col and row
            board[pos[0]] = [-1 for _ in range(n)]
            for i in range(n):
                board[i][pos[1]] = -1
            if pos[0] - 1 >= 0 and pos[1] - 1 >= 0:
                board[pos[0] - 1][pos[1] - 1] = -1
            if pos[0] + 1 < n and pos[1] + 1 < n:
                board[pos[0] + 1][pos[1] + 1] = -1
            if pos[0] + 1 < n and pos[1] - 1 >= 0:
                board[pos[0] + 1][pos[1] - 1] = -1
            if pos[0] - 1 >= 0 and pos[1] + 1 < n:
                board[pos[0] - 1][pos[1] + 1] = -1
            return board

        def get_pos_move(board):
            pos_move = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] != -1:
                        pos_move.append([i, j])
            return pos_move

        def backtrack(board, reminding_q):
            if reminding_q == 0:
                result = +1
            pos_move = get_pos_move(board)
            if not pos_move:
                return
            for _m in pos_move:
                n_board = q_coverage(board[::], _m)
                backtrack(n_board[::], reminding_q - 1)

        board = [[1 for _ in range(n)] for _ in range(n)]
        backtrack(board[::], n)
        return result


solution = Solution()
print(solution.totalNQueens(5))
