from typing import List
import math


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        dec_temp = []
        i = 0
        while i != len(temperatures) - 1:
            if temperatures[i] >= temperatures[i + 1]:
                dec_temp.append((temperatures[i], i))
            else:
                result[i] = 1
                while dec_temp:
                    _temp, _i = dec_temp.pop(-1)
                    if _temp < temperatures[i + 1]:
                        result[_i] = i + 1 - _i
                    else:
                        dec_temp.append((_temp, _i))
                        break
            i += 1
        return result


solution = Solution()
print(solution.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
