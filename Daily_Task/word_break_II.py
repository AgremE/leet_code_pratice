from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        result = []
        self._backtrack(s, word_set, result, [], 0)
        return result

    def _backtrack(self, s, word_set, result, current_set, start_ind):
        if start_ind == len(s):
            result.append(" ".join(current_set))
            return
        for end_ind in range(start_ind + 1, len(s) + 1):
            word = s[start_ind:end_ind]
            if word in word_set:
                current_set.append(word)
                self._backtrack(s, word_set, result, current_set, end_ind)
                current_set.pop()
