from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def get_possible_move(self, maz, cur_pos, track_visitor):
        pos_x, pos_y = cur_pos
        result = []
        if (
            (pos_x - 1 >= 0)
            and (maz[pos_x - 1][pos_y] != "+")
            and track_visitor[pos_x - 1][pos_y] != 1
        ):
            result.append([pos_x - 1, pos_y])
            track_visitor[pos_x - 1][pos_y] = 1
        if (
            (pos_x + 1 < len(maz))
            and (maz[pos_x + 1][pos_y] != "+")
            and track_visitor[pos_x + 1][pos_y] != 1
        ):
            result.append([pos_x + 1, pos_y])
            track_visitor[pos_x + 1][pos_y] = 1
        if (
            (pos_y - 1 >= 0)
            and (maz[pos_x][pos_y - 1] != "+")
            and track_visitor[pos_x][pos_y - 1] != 1
        ):
            result.append([pos_x, pos_y - 1])
            track_visitor[pos_x][pos_y - 1] = 1
        if (
            (pos_y + 1 < len(maz[0]))
            and (maz[pos_x][pos_y + 1] != "+")
            and track_visitor[pos_x][pos_y + 1] != 1
        ):
            result.append([pos_x, pos_y + 1])
            track_visitor[pos_x][pos_y + 1] = 1
        return result, track_visitor

    def is_finish(self, move, maz, entrance):
        x, y = move
        max_x, max_y = len(maz), len(maz[0])
        if x == entrance[0] and y == entrance[1]:
            return False
        if x == max_x - 1 or y == max_y - 1 or x == 0 or y == 0:
            return True
        return False

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ## Reverse
        transposed_tuples = list(zip(*maze))
        # This looks like: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        maze = [list(sublist) for sublist in transposed_tuples]
        entrance[0], entrance[1] = entrance[1], entrance[0]
        track_visitor = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        track_visitor[entrance[0]][entrance[1]] = 1
        heap = []
        heapify(heap)
        possible_move, track_visitor = self.get_possible_move(
            maze, entrance, track_visitor
        )
        result = 0
        for _mov in possible_move:
            if self.is_finish(_mov, maze, entrance):
                result = result + 1
                return result
            heappush(heap, (1, [_mov[0], _mov[1]]))
        while heap:
            cur_best_move = heappop(heap)
            score, _move = cur_best_move
            cur_possible_move, track_visitor = self.get_possible_move(
                maze, _move, track_visitor
            )
            for move in cur_possible_move:
                if self.is_finish(move, maze, entrance):
                    result = score + 1
                    return result
                heappush(heap, (score + 1, [_move[0], _move[1]]))
        return -1


solution = Solution()
print(
    solution.nearestExit(
        [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
        entrance=[1, 2],
    )
)

print(
    solution.nearestExit(
        maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance=[1, 0]
    )
)
print(solution.nearestExit(maze=[[".", "+"]], entrance=[0, 0]))
