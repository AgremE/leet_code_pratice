from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w_1 = ("").join(word1)
        w_2 = ("").join(word2)
        if len(w_1) != len(w_2):
            return False
        result = w_1
        for word in word2:
            result = result.replace(word, "", 1)
        if result == "":
            return True
        return False


word1 = ["jbboxe", "yshcrtanrtlzyyp", "vudsssnzuef", "lde"]
word2 = ["jbboxeyshcrtanrt", "lzyypvudsssnzueflde"]
solution = Solution()
print(solution.arrayStringsAreEqual(word1, word2))
