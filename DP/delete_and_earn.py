from typing import List
from collections import Counter


def deleteAndEarn(nums: List[int]) -> int:
    count_num = Counter(nums)
    unique_set = list(set(nums))
    unique_set.sort(reverse=True)
    len_num = len(unique_set)
    max_result = unique_set[0] * count_num[unique_set[0]]
    curr_elem = unique_set[0]
    print(count_num)
    for i in range(1, len_num - 1):
        if curr_elem == unique_set[i] + 1 or curr_elem == unique_set[i + 1]:
            pre_pick = unique_set[i - 1] * count_num[unique_set[i - 1]]
            curr_pick = unique_set[i] * count_num[unique_set[i]]
            if pre_pick < curr_pick:
                max_result = max_result - pre_pick + curr_pick
                curr_elem = unique_set[i]
        else:
            max_result = max_result + unique_set[i] * count_num[unique_set[i]]
            curr_elem = unique_set[i]
    return max_result


def deleteAndEarnSecond(nums):
    count_num = Counter(nums)
    unique_set = list(set(nums))
    unique_set.sort(reverse=True)
    l_num = len(unique_set)
    reward_map = [[0 for _ in range(2)] for _ in range(l_num)]
    reward_map[0][1] = unique_set[0] * count_num[unique_set[0]]
    reward_map[0][0] = 0
    for i in range(1, l_num):
        curr_pick = unique_set[i] * count_num[unique_set[i]]
        if unique_set[i] == unique_set[i - 1] - 1:
            reward_map[i][0] = max(reward_map[i - 1][0], reward_map[i - 1][1])
            reward_map[i][1] = max(
                reward_map[i - 1][0] + curr_pick, reward_map[i - 1][1]
            )
        else:

            reward_map[i][0] = max(reward_map[i - 1][0], reward_map[i - 1][1])
            reward_map[i][1] = max(
                reward_map[i - 1][0] + curr_pick, reward_map[i - 1][1] + curr_pick
            )
    return max(reward_map[l_num - 1][0], reward_map[l_num - 1][1])


print(deleteAndEarnSecond([8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4]))
# print(deleteAndEarnSecond([1, 1, 1, 2, 4, 5, 5, 5, 6]))
