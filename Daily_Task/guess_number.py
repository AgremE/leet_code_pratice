# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
guess_num = 1


def guess(num: int) -> int:
    if num > guess_num:
        return -1
    elif num < guess_num:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        upper_bound = n
        lower_boud = 0
        if guess(n) == 0:
            return n
        while True:
            mid_num = lower_boud + (upper_bound - lower_boud) // 2
            guess_result = guess(mid_num)
            if guess_result == -1:
                upper_bound = mid_num
            elif guess_result == 1:
                lower_boud = mid_num
            else:
                return mid_num


solution = Solution()
print(solution.guessNumber(10))
