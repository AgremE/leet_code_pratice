from typing import List
import math
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        default_char = {char:i+1 for i,char in enumerate("abcdefghijklmnopqrstuvwxyz")}
        value_char = []
        dic_char = {chars[i]:vals[i] for i in range(len(vals))}
        for _c in s:
            if _c in dic_char:
                value_char.append(dic_char[_c])
            else:
                value_char.append(default_char[_c])
        # the problem now translate to max sum sub array
        s_i, f_i = 0,0
        _max = -math.inf
        _cur_sum = 0
        while f_i!=len(value_char):
            if s_i == f_i:
                if value_char[s_i]<0:
                    _cur_sum = value_char[s_i]
                    s_i+=1
                    f_i+=1
                else:
                    _cur_sum = value_char[s_i]
                    f_i+=1
            else:
                _cur_sum+=value_char[f_i]
                if _cur_sum>0:
                    f_i+=1
                else:
                    s_i = f_i
            if _cur_sum>_max:
                _max = _cur_sum
        return _max
            

