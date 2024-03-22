class Solution:
    def numTilings(self, n: int) -> int:
        def recurve(n, memoir):
            if n in memoir:
                return memoir[n]
            if n < 3:
                return n
            elif n == 3:
                return 5

            memoir[n] = (
                5 * recurve(n - 3, memoir)
                + 2 * recurve(n - 2, memoir)
                + recurve(n - 1, memoir)
            )
            return memoir[n]

        memoir = {}
        return recurve(n, memoir)
