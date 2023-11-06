from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_each_index = []
        for i in range(len(nums)):
            curr_num = nums[i]
            len_tracker = 10**6
            assing = False
            if curr_num >= target:
                assing = True
                return 1
            else:
                for x in range(i + 1, len(nums)):
                    curr_num = curr_num + nums[x]
                    if curr_num >= target:
                        len_tracker = x - i + 1
                        assing = True
                        break
            if assing:
                len_each_index.append(len_tracker)
        if len_each_index:
            return min(len_each_index)
        else:
            return 0


solution = Solution()
print(solution.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(solution.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
