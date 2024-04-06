class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        flip = {}
        for i in range(len(s)):
            _c = s[i]
            if _c in flip:
                if flip[_c] != t[i]:
                    return False
            else:
                flip[_c] = t[i]
        duplication = set()
        for key, val in flip.items():
            if val in duplication:
                return False
            duplication.add(val)
        return True
