from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s_i, f_i = 0, 0
        neg_stack = []
        pos_stack = []
        while s_i != len(asteroids):
            astr = asteroids[s_i]
            if astr > 0:
                pos_stack.append(astr)
            else:
                _set = False
                while pos_stack:
                    pos_astr = pos_stack.pop(-1)
                    if abs(pos_astr) >= abs(astr):
                        if abs(pos_astr) > abs(astr):
                            pos_stack.append(pos_astr)
                        _set = True
                        break
                    _set = False
                if not _set:
                    neg_stack.append(astr)
            s_i += 1
        return neg_stack + pos_stack


solution = Solution()
print(solution.asteroidCollision([10, 2, -5]))
