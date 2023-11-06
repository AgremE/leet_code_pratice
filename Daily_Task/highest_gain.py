from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        _max = 0
        _curr = 0
        for num in gain:
            _curr = _curr + num
            if _max < _curr:
                _max = _curr
        return _max


solution = Solution()
print(solution.largestAltitude(gain=[-5, 1, 5, 0, -7]))
