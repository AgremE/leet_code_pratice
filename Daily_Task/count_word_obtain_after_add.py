from typing import List


class Solution:
    def can_converse(self, startWord, targetWord):
        _s_word = {}
        _t_word = {}
        for _s in startWord:
            if _s in _s_word:
                _s_word[_s] = _s_word[_s] + 1
            else:
                _s_word[_s] = 1
        for _t in targetWord:
            if _t in _t_word:
                _t_word[_t] = _t_word[_t] + 1
            else:
                _t_word[_t] = 1
        for _s_key, _s_value in _s_word.items():
            if _s_key not in _t_word:
                return False
            else:
                _t_value = _t_word[_s_key]
                if _t_value != _s_value:
                    return False
        return True

    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        result = []
        for _t in targetWords:
            for _s in startWords:
                if len(_s) == len(_t):
                    continue
                if self.can_converse(_s, _t):
                    result.append(1)
                    break
        return sum(result)


solution = Solution()
print(
    solution.wordCount(
        startWords=["ant", "act", "tack"], targetWords=["tack", "act", "acti"]
    )
)
print(solution.wordCount(startWords=["ab", "a"], targetWords=["abc", "abcd"]))
