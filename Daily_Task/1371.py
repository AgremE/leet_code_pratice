


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        v = set([ 'a', 'e', 'i', 'o', 'u' ])
        





##  
# Brute force the solution
# #
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def _check(tracker):
            for _,count in tracker.items():
                if count%2==1:
                    return False
            return True
        v = set([ 'a', 'e', 'i', 'o', 'u' ])
        _max = 0
        tracker = {}
        for i in range(len(s)):
            tracker = {}
            if s[i] in v:
                tracker[s[i]]=1
                temp_max = 0 
            else:
                tracker = {}
                temp_max = 1 
            for j in range(i+1,len(s)):
                if s[j] in v:
                    tracker[s[j]] = tracker.get(s[j],0)+1
                if _check(tracker):
                    temp_max = max(temp_max,j-i+1)
            _max = max(_max,temp_max)
        return _max
