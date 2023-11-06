from typing import List
import math


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        len_arr = len(nums)
        if len_arr == 1:
            return 0
        len_first_avg = 1
        first_average = nums[0] / len_first_avg
        len_second = len_arr - 1
        second_average = sum(nums[1:]) / len_second
        result = [abs(math.floor(first_average) - math.floor(second_average))]
        for i in range(1, len_arr):
            ### update first average
            total_sum_first = first_average * len_first_avg
            len_first_avg = len_first_avg + 1
            first_average = (total_sum_first + nums[i]) / len_first_avg
            ### update second average
            total_sum_second = second_average * len_second
            len_second = len_second - 1
            if len_second == 0:
                result.append(first_average)
                continue
            second_average = (total_sum_second - nums[i]) / len_second
            result.append(abs(math.floor(first_average) - math.floor(second_average)))
        print(result)
        index_min = min(range(len(result)), key=result.__getitem__)
        return index_min


solution = Solution()
# print(solution.minimumAverageDifference(nums=[2, 5, 3, 9, 5, 3]))
print(solution.minimumAverageDifference(nums=[99999, 0, 0, 0, 0, 0, 0, 0]))
