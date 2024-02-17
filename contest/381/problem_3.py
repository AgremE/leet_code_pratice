from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def get_n_v(start, n, x, y):
            n_v = []
            if start == x:
                n_v.append(y)
            if start == y:
                n_v.append(x)
            temp_v = [start - 1, start + 1]
            n_v = n_v + [_x for _x in temp_v if _x > 0 and _x < n + 1]
            return n_v

        def bfs(start, n, x, y):
            level = [0]
            next_v = [start]
            temp_n_v = []
            alread_v = {}
            while next_v:
                _v = next_v.pop()
                if _v in alread_v:
                    continue
                alread_v[_v] = 1
                level[-1] += 1
                temp_n_v += get_n_v(start, n, x, y)
                if next_v == []:
                    level.append(0)
                    next_v = temp_n_v
                    temp_n_v = []
            return level

        temp_result = []
        for i in range(n):
            temp_result.append(bfs(i, n, x, y))
        result = [0 for _ in range(n)]
        for i in range(n):
            _sum = sum([x[i] for x in temp_result])
            result[i] += _sum
        return result


solution = Solution()
print(solution.countOfPairs(n=5, x=2, y=4))
