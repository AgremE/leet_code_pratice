"""

        # too slow in the running time
        def is_palindrom(s: str):
            len_s = len(s)
            if len_s == 1:
                return True
            half_len = len_s // 2
            if len_s % 2 == 1:
                if s[:half_len] == s[half_len + 1 :][::-1]:
                    return True
            else:
                if s[:half_len] == s[half_len:][::-1]:
                    return True
            return False

        max_palindrom = 0
        result = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                cur_str = s[i:j]
                if is_palindrom(cur_str):
                    if max_palindrom < j - i:
                        max_palindrom = j - i
                        result = cur_str
        return result
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Using two-d array to help out
        pass


solution = Solution()
print(solution.longestPalindrome("aacabdkacaa"))
