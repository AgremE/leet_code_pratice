class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        def partial_recur(n, memoir_paritial, memoir_full):
            if n in memoir_paritial:
                return memoir_paritial[n]
            if n == 2:
                return 1
            memoir_paritial[n] = partial_recur(
                n - 1, memoir_paritial, memoir_full
            ) + full_recur(n - 2, memoir_paritial, memoir_full)
            memoir_paritial[n] = memoir_paritial[n] % MOD
            return memoir_paritial[n]

        def full_recur(n, memoir_paritial, memoir_full):
            if n in memoir_full:
                return memoir_full[n]
            if n < 3:
                return n
            memoir_full[n] = (
                2 * partial_recur(n - 1, memoir_paritial, memoir_full)
                + full_recur(n - 1, memoir_paritial, memoir_full)
                + full_recur(n - 2, memoir_paritial, memoir_full)
            )
            memoir_full[n] = memoir_full[n] % MOD
            return memoir_full[n]

        memoir_paritial = {}
        memoir_full = {}
        return full_recur(n, memoir_paritial, memoir_full)
