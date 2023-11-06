from  collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        s1counter = Counter(s1)
        s2counter = Counter()
        for i in range(len_s2):
            s2counter[s2[i]]+=1
            if i > len_s1-1:
                if s2counter[s2[i-len_s1]] == 1:
                    del s2counter[s2[i-len_s1]]
                else:
                    s2counter[s2[i-len_s1]] -= 1
            if s1counter == s2counter:
                return True
        return False
        

test = Solution()

print(test.checkInclusion("adc","dcda"))