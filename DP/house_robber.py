from typing import List


def rob(nums: List[int]) -> int:
    len_num = len(nums)
    reward_map = [[0 for x in range(2)] for y in range(len_num)]
    reward_map[0][1] = nums[0]
    reward_map[0][0] = 0
    for i in range(1, len_num):
        reward_map[i][1] = reward_map[i - 1][0] + nums[i]
        reward_map[i][0] = max(reward_map[i - 1][1], reward_map[i - 1][0])
    return max(reward_map[len_num - 1][1], reward_map[len_num - 1][0])


print(rob([2, 7, 9, 100, 1]))
