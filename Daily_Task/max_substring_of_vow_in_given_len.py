import math
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        all_vow = set(['a', 'e', 'i', 'o', 'u'])
        _max = -math.inf
        _temp_max = 0
        for i in range(k):
            if s[i] in all_vow:
                _temp_max +=1
        if _temp_max > _max:
            _max=_temp_max
        for i in range(1,len(s)-k+1):
            if s[i-1] in all_vow:
                _temp_max-=1
            if s[i+k-1] in all_vow:
                _temp_max+=1
            if _temp_max > _max:
                _max = _temp_max
        return _max

solution = Solution()
print(solution.maxVowels(s = "weallloveyou", k = 7))