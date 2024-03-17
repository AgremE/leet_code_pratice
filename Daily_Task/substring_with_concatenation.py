"""
Problem description:

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        start_w = {}
        for word in words:
            if word[0] in start_w:
                start_w[word[0]].append(word)
            else:
                start_w[word[0]] = [word]

        def is_start_indice(s, start_w):
            ls_ws = start_w[s[0]]
            for w in ls_ws:
                pass
