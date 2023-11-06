from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # result_win = {}
        result_loss = {}
        unique_player = {}
        for match in matches:
            win, loss = match
            if not win in unique_player:
                unique_player[win] = 1
            if not loss in unique_player:
                unique_player[loss] = 1
            if loss in result_loss:
                result_loss[loss] = result_loss[loss] + 1
            else:
                result_loss[loss] = 1
        result = [[] for x in range(2)]
        for player, loss_num in result_loss.items():
            if loss_num == 1:
                result[1].append(player)
        for player, id in unique_player.items():
            if not (player in result_loss):
                result[0].append(player)
        result[0].sort()
        result[1].sort()
        return result


solution = Solution()
print(
    solution.findWinners(
        [
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    )
)
