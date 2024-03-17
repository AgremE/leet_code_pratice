class Solution(object):
    def colorRed(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def generate_tile_at_lvl(lvl):
            num_tile = lvl * 2 - 1
            _tile = 1
            result = []
            while _tile < num_tile:
                result.append([lvl, _tile])
                _tile += 4
                if _tile >= num_tile:
                    result.append([lvl, num_tile - 2])
                    result.append([lvl, num_tile - 1])
            return result

        if n == 1:
            return [[1, 1]]
        elif n == 2:
            return [[1, 1], [2, 1], [2, 3]]
        result = [[1, 1], [2, 1], [2, 3]]
        for lvl in range(2, n + 1):
            result += generate_tile_at_lvl(lvl)
        return result
