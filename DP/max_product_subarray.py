from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _min = nums[0]
        _max = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curr_max = max(_max * num, _min * num)
            curr_min = min(_max * num, _min * num)
            if curr_max >= _max:
                _max = curr_max
            if curr_min <= _min:
                _min = curr_min
            print(f"Current Min: {_max}")
            print(f"Current Max: {_min}")
        return _max, _min


solution = Solution()
# print(solution.maxProduct([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]))
print(solution.maxProduct([2, 3, -2, 4]))
# print(solution.maxProduct([-2, 0, -1]))
# print(solution.maxProduct([-2, 3, -2]))
