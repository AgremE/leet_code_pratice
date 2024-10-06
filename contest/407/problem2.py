class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow = ["a", "e", "i", "o", "u"]
        test = set(s)
        for v in vow:
            if v in test:
                return True
        return False
