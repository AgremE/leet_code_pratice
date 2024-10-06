class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        i, f = 0, 0
        tracker = set()
        count = 0
        while tracker:
            if s[f] in tracker or f == len(s) - 1:
                # moving i
                while i != f:
                    i += 1
                    tracker.remove(s[i])
                    count += 1
            else:
                count += 1
                f += 1
                tracker.add(s[f])
        return count
