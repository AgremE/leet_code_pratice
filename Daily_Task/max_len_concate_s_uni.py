from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uni_list = []
        for elem in arr:
            set_elem = set(elem)
            if len(elem) == len(set_elem):
                uni_list.append(set_elem)
        tracker = [set()]
        for elem_char in uni_list:
            for trac in tracker:
                if not trac & elem_char:
                    tracker.append(trac | elem_char)
        return max([len(elem) for elem in tracker])


solution = Solution()
print(solution.maxLength(["un", "iq", "ue"]))
print(solution.maxLength(["cha", "r", "act", "ers"]))
print(solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
