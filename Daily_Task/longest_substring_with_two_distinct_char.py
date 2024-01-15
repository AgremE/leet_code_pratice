from collections import Counter


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        def get_counter_order(s):
            _s_char = s[0]
            count = 0
            result = []
            for i in range(len(s)):
                if _s_char == s[i]:
                    count += 1
                else:
                    result.append((_s_char, count))
                    _s_char = s[i]
                    count = 1
                if i == len(s) - 1:
                    result.append((_s_char, count))
            return result

        counter = get_counter_order(s)
        char_count = {}
        _temp_max = 0
        _max = -1
        for i in range(len(counter)):
            char, count = counter[i]
            char_count[char] = 1
            if len(char_count) <= 2:
                _temp_max += count
            else:
                if _temp_max > _max:
                    _max = _temp_max
                char_count = {char: 1, counter[i - 1][0]: 1}
                _temp_max = count + counter[i - 1][1]
        if _temp_max > _max:
            _max = _temp_max
        return _max


solution = Solution()
# print(solution.lengthOfLongestSubstringTwoDistinct("eceba"))
print(solution.lengthOfLongestSubstringTwoDistinct("a"))
# print(solution.lengthOfLongestSubstringTwoDistinct("aba"))
