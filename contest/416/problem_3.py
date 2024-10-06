import collections
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        f_i, s_i = 0,0
        cw2 = collections.Counter(word2)
        def _check(cw1,cw2):
            for w, c in cw2.items():
                if w not in cw1:
                    return False
                if c > cw1[w]:
                    return False
            return True
        total_count = 0
        cw1 = {}
        while s_i!=len(word1):
            cw1[word1[s_i]] = cw1.get(word1[s_i],0) + 1
            s_i+=1
            if _check(cw1,cw2):
                total_count+=1
        while f_i!=len(word1):
            cw1[word1[f_i]] = cw1.get(word1[f_i],0) - 1
            f_i+=1
            if _check(cw1,cw2):
                total_count+=1
        return total_count

solution = Solution()
print(solution.validSubstringCount(word1 = "abcabc", word2 = "abc"))
