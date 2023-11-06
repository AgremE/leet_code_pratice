from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict_count = {}
        len_num = len(nums)
        len_compare = math.floor(len_num / 3)
        for num in nums:
            if num in dict_count:
                dict_count[num] = dict_count[num] + 1
            else:
                dict_count[num] = 1
        result = []
        for key, value in dict_count.items():
            if value > len_compare:
                result.append(key)
        return result


solution = Solution()
# print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([1]))
print(solution.majorityElement([1, 2]))
