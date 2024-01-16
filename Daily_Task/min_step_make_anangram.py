class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        result = 0
        for _k, _count in s_count.items():
            if _k in t_count and t_count[_k] != 0:
                _count = max(_count - t_count[_k], 0)
                s_count[_k] = _count
            result += s_count[_k]
        return result
