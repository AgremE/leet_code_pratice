# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
version = [False, False, False, False, False, True, True, True, True]


def isBadVersion(n):
    return version[n]


class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid_idx = n // 2
        left = 0
        right = n - 1
        while left <= right:
            status = isBadVersion(mid_idx)
            if status:
                right = mid_idx - 1
                mid_idx = (right + left) // 2
            else:
                left = mid_idx + 1
                mid_idx = (right + left) // 2
        return left


test_solution = Solution()
print(test_solution.firstBadVersion(9))
