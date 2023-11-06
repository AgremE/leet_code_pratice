from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic_count = {}
        for num in tasks:
            if num in dic_count:
                dic_count[num] = dic_count[num] + 1
            else:
                dic_count[num] = 1
        total_round = 0
        for dif, num in dic_count.items():
            if num == 1:
                return -1
            else:
                temp_round = num // 3
                reminding_round = num - temp_round * 3
                if reminding_round == 1 or reminding_round == 2:
                    temp_round = temp_round + 1
                total_round = total_round + temp_round
        return total_round


solution = Solution()
print(solution.minimumRounds([2, 3, 3]))
