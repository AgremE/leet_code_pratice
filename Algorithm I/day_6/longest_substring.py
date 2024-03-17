class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_str = ""
        max_len = 0
        for i in range(len(s)):
            longest_str = s[i]
            for j in range(i + 1, len(s)):
                if s[j] in longest_str:
                    break
                longest_str = longest_str + s[j]
            if len(longest_str) > max_len:
                max_len = len(longest_str)
        return max_len


test_solution = Solution()
print(test_solution.lengthOfLongestSubstring("abcabcbb"))
