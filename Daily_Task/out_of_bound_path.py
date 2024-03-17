class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        def get_next(m, n, c_r, c_c):
            result = []
            result = [
                [c_r - 1, c_c],
                [c_r + 1, c_c],
                [c_r, c_c + 1],
                [c_r, c_c - 1],
            ]
            return [
                x for x in result if x[0] >= 0 and x[0] < m and x[1] >= 0 and x[1] < n
            ]

        def is_out_bound(m, n, c_r, c_c):
            if c_r >= m or c_r < 0:
                return True
            if c_c >= n or c_c < 0:
                return True
            return False

        def get_score(m, n, c_r, c_c):
            result = []
            result = [
                [c_r - 1, c_c],
                [c_r + 1, c_c],
                [c_r, c_c + 1],
                [c_r, c_c - 1],
            ]
            return 4 - len(
                [x for x in result if x[0] >= 0 and x[0] < m and x[1] >= 0 and x[1] < n]
            )

        start_v = {(startRow, startColumn): 1}
        n_v = []
        result = 0
        MOD = 10**9 + 7
        for i in range(maxMove):
            vertex_count = {}
            for _pair, _count in start_v.items():
                _s = get_score(m, n, _pair[0], _pair[1])
                result = result + _s * _count
                n_v = get_next(m, n, _pair[0], _pair[1])
                for _p in n_v:
                    if not ((_p[0], _p[1]) in vertex_count):
                        vertex_count[(_p[0], _p[1])] = _count
                    else:
                        vertex_count[(_p[0], _p[1])] += _count
            start_v = vertex_count

        return result % MOD


solution = Solution()
# print(solution.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
print(solution.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
