from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_start_w = {}
        len_s = len(s)
        matrix_tracker = [0 for _ in range(len_s)]
        for word in wordDict:
            start_c = word[0]
            if start_c in word_start_w:
                word_start_w.append(word)
            else:
                word_start_w[start_c] = [word]
        matrix_tracker[0] = 1
        for i in range(len_s):
            start_c_s = s[i]
            if matrix_tracker[i] == 1:
                possible_words = word_start_w[start_c_s]
                for _word in possible_words:
                    len_word = len(_word)
                    if _word == s[i : i + len_word]:
                        if i + len_word == len_s:
                            return True
                        elif i + len_word <= len_s - 1:
                            matrix_tracker[i + len_word] = 1
        return False


solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))
