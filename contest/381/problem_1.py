from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        _count = Counter(list(word))
        _char_count = sorted([_c for _k, _c in _count.items()], reverse=True)
        next_count = 8
        init = 1
        result = 0
        for i in _char_count:
            result += init * i
            next_count -= 1
            if next_count == 0:
                next_count = 8
                init += 1
        return result


solution = Solution()
print(solution.minimumPushes(word="acolkxjbizfmhnrdq"))
