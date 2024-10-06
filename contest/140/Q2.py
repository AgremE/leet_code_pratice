from typing import List
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight = sorted(maximumHeight,reverse=True)
        _cur_max = maximumHeight[0]
        _result = _cur_max
        for i in range(1,len(maximumHeight)):
            _temp_max = maximumHeight[i]
            if _temp_max<_cur_max:
                _cur_max = _temp_max
                _result+=_cur_max
            else:
                _cur_max-=1
                if _cur_max==0:
                    return -1
                else:
                    _result+=_cur_max
        return _result