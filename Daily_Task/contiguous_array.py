from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_countinue = [1]
        init_num = nums[0]
        for i in range(1, len(nums)):
            if init_num == nums[i]:
                count_countinue[-1] += 1
            else:
                init_num = nums[i]
                count_countinue.append(1)
        reminding = 0
        for i in range(1, len(count_countinue)):
            temp_reminding = count_countinue[i + 1] - count_countinue[i]
