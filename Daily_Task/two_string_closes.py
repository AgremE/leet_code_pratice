class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict_word_1 = {}
        dict_word_2 = {}
        for _w in word1:
            if _w in dict_word_1:
                dict_word_1[_w] = dict_word_1[_w] + 1
            else:
                dict_word_1[_w] = 1
            if _w not in word2:
                return False
        for _w in word2:
            if _w in dict_word_2:
                dict_word_2[_w] = dict_word_2[_w] + 1
            else:
                dict_word_2[_w] = 1
            if _w not in word1:
                return False
        value_list_word1 = list(dict_word_1.values())
        value_list_word2 = list(dict_word_2.values())
        if len(value_list_word1) != len(value_list_word2):
            return False
        value_list_word1.sort()
        value_list_word2.sort()
        for i in range(len(value_list_word1)):
            if value_list_word1[i] != value_list_word2[i]:
                return False
        return True


solution = Solution()
print(solution.closeStrings(word1="abc", word2="bca"))
print(solution.closeStrings(word1="cabbba", word2="abbccc"))
print(solution.closeStrings(word1="cb", word2="cb"))
###False
print(solution.closeStrings(word1="c", word2="b"))
print(solution.closeStrings(word1="cc", word2="bb"))
print(solution.closeStrings(word1="abbzzca", word2="babzzcz"))
