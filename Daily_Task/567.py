import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        counter_s1 = collections.Counter(s1)
        counter_s2 = collections.Counter(s2[:len(s1)])
        f_i, s_i = 0,0
        f_i,s_i = 0, len(s1)-1
        while s_i!=len(s2):
            if not counter_s1 == counter_s2:
                s_i+=1
                if s_i == len(s2):
                    break
                counter_s2[s2[s_i]] = counter_s2.get(s2[s_i],0)+1
                counter_s2[s2[f_i]]-=1
                if counter_s2[s2[f_i]] == 0:
                    counter_s2.pop(s2[f_i],0)
                f_i+=1
            else:
                return True
        return False
    

solution = Solution()
print( 
    solution.checkInclusion("ab","eidbaooo")
)