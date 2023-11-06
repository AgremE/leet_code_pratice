from typing import List


def rob(nums: List[int]) -> int:
    no_f_h = nums[1:]
    no_l_h = nums[:-1]
    len_loop = len(nums) - 1
    reward_map_no_f_h = [[0 for x in range(2)] for y in range(len_loop)]
    reward_map_no_f_h[0][1] = no_f_h[0]
    reward_map_no_f_h[0][0] = 0
    for i in range(1, len_loop):
        reward_map_no_f_h[i][1] = reward_map_no_f_h[i - 1][0] + no_f_h[i]
        reward_map_no_f_h[i][0] = max(
            reward_map_no_f_h[i - 1][1], reward_map_no_f_h[i - 1][0]
        )
    max_reward_no_f_h = max(
        reward_map_no_f_h[len_loop - 1][1], reward_map_no_f_h[len_loop - 1][0]
    )
    reward_map_no_l_h = [[0 for x in range(2)] for y in range(len_loop)]
    reward_map_no_l_h[0][1] = no_l_h[0]
    reward_map_no_l_h[0][0] = 0
    for i in range(1, len_loop):
        reward_map_no_l_h[i][1] = reward_map_no_l_h[i - 1][0] + no_l_h[i]
        reward_map_no_l_h[i][0] = max(
            reward_map_no_l_h[i - 1][1], reward_map_no_l_h[i - 1][0]
        )
    max_reward_no_l_h = max(
        reward_map_no_l_h[len_loop - 1][1], reward_map_no_l_h[len_loop - 1][0]
    )
    return max(max_reward_no_f_h, max_reward_no_l_h)


print(rob([1, 2, 3, 1]))
