import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        can_remove = {}
        total_remove = 0
        for _c, _count in t_count.items():
            if not (_c in s_count):
                return ""
            if s_count[_c] - t_count[_c] < 0:
                return ""
            can_remove[_c] = s_count[_c] - t_count[_c]
            total_remove += can_remove[_c]
        # Using DP to check overall result
        l_i = 0
        r_i = 0
        cur_min = s
        while True:
            r_c = s[r_i]
            if r_c in can_remove:
                if can_remove[r_c] > 0:
                    can_remove[r_c] -= 1
            if sum(can_remove.values()) == 0:
                # start remove left
                while True:
                    l_c = s[l_i]
                    if not (l_c in can_remove):
                        l_c += 1


solution = Solution()
print(solution.minWindow(s="cabwefgewcwaefgcf", t="cae"))
