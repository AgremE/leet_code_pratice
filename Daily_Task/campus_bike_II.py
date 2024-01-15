from typing import List
import math


class Solution:
    def __init__(self) -> None:
        self.smallest = math.inf
        self.assignBikesList = []

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.assignBikesList = [0 for _ in range(len(bikes))]

        def get_distance(w_co, b_co):
            return abs(w_co[0] - b_co[0]) + abs(w_co[1] - b_co[1])

        def recurv(workers, bikes, w_i, cur_distance):
            if cur_distance >= self.smallest:
                return None
            if w_i >= len(workers):
                self.smallest = min(cur_distance, self.smallest)
                return None
            for b_i in range(len(bikes)):
                if self.assignBikesList[b_i] != 1:
                    self.assignBikesList[b_i] = 1
                    recurv(
                        workers,
                        bikes,
                        w_i + 1,
                        cur_distance + get_distance(workers[w_i], bikes[b_i]),
                    )
                    self.assignBikesList[b_i] = 0

        recurv(workers, bikes, 0, 0)
        return self.smallest


solution = Solution()
# print(solution.assignBikes(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]))
print(
    solution.assignBikes(
        workers=[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
        bikes=[[0, 999], [1, 999], [2, 999], [3, 999], [4, 999]],
    )
)
