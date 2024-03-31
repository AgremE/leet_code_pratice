import math


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        tracker = {}
        s_i, f_i = 0, 0
        _max = -math.inf
        while f_i < len(s):
            _c = s[f_i]
            if _c in tracker:
                f_i += 1
                tracker[_c] += 1
            else:
                tracker[_c] = 1
                while len(tracker) > k:
                    tracker[s_i] -= 1
                    if tracker[s_i] == 0:
                        del tracker[s_i]
                _max = max(_max, f_i - s_i + 1)
        return _max
