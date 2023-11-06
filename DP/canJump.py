from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ind_zero = []
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                ind_zero.append(i)
        ind_zero.sort()
        len_num = len(nums)
        if not ind_zero or len_num == 1:
            return True
        for x in range(len(ind_zero)):
            i_0 = ind_zero[x]
            can_jump = False
            for y in range(i_0):
                if (nums[y] - (i_0 - y) > 0) or (
                    (nums[y] + y - i_0 == 0) and (i_0 == len_num - 1) and (nums[y] != 0)
                ):
                    can_jump = True
            if not can_jump:
                return False
        return True


solution = Solution()

print(solution.canJump([1, 1, 1, 0]))
