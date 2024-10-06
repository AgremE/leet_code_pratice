from typing import List


class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        horizontalCut = sorted(horizontalCut)
        verticalCut = sorted(verticalCut)
        ver_split = 0
        hor_split = 0
        cost = 0
        while horizontalCut or verticalCut:
            if not verticalCut:
                cost += sum([x * (ver_split + 1) for x in horizontalCut])
                break
            if not horizontalCut:
                cost += sum([x * (hor_split + 1) for x in verticalCut])
                break
            if horizontalCut[-1] > verticalCut[-1]:
                cost += horizontalCut[-1] * (ver_split + 1)
                hor_split += 1
                horizontalCut.pop()
            else:
                cost += verticalCut[-1] * (hor_split + 1)
                ver_split += 1
                verticalCut.pop()
        return cost


solution = Solution()
print(solution.minimumCost(m=6, n=3, horizontalCut=[2, 3, 2, 3, 1], verticalCut=[1, 2]))
