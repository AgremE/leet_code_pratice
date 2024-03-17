class Solution:
    def customSortString(self, order: str, s: str) -> str:
        key_order = {}
        for i, char in enumerate(order):
            key_order[char] = i
        sorted_string = []
        unsorted_string = []
        for _c in s:
            if _c in key_order:
                sorted_string.append((_c, key_order[_c]))
            else:
                unsorted_string.append(_c)
        sorted_string = sorted(sorted_string, key=lambda x: x[1])
        return "".join(x[0] for x in sorted_string) + "".join(unsorted_string)
