from typing import List
import math


class Solution:
    def maximumLength(self, s: str) -> int:
        result = {}
        i = 0
        _count = 1
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                _count += 1
            else:
                if s[i] in result:
                    result[s[i]].append(_count)
                    _count = 1
                else:
                    result[s[i]] = [_count]
                    _count = 1
            i = i + 1
            if i == len(s) - 1:
                if s[i] in result:
                    result[s[i]].append(_count)
                    _count = 1
                else:
                    result[s[i]] = [_count]
                    _count = 1

        _max = -math.inf
        for c, list_count in result.items():
            temp_list = sorted(list_count)
            if len(temp_list) >= 2:
                if temp_list[-1] - temp_list[-2] == 1 or (
                    temp_list[-1] - temp_list[-2] == 0 and temp_list[-1] != 1
                ):
                    if temp_list[-1] - 1 > _max:
                        _max = temp_list[-1] - 1
                        continue
            if temp_list[-1] - 2 > 0:
                if temp_list[-1] - 2 > _max:
                    _max = temp_list[-1] - 2
                    continue
            if len(temp_list) < 3:
                if sum(temp_list) >= 3:
                    if _max < 1:
                        _max = 1
                continue
            temp = min(temp_list[-3:])
            if temp > _max:
                _max = temp
        return -1 if _max == -math.inf else _max


solution = Solution()
print(solution.maximumLength(s="iiiiifffffffoooookkkfffffffnnxxxxxx"))
