class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        ### Shift entire coord to positive
        min_x = min([ax1, ax2, bx1, bx2])
        min_y = min([ay1, ay2, by1, by2])
        if min_x < 0:
            ax1 = ax1 - min_x
            ax2 = ax2 - min_x
            bx1 = bx1 - min_x
            bx2 = bx2 - min_x
        if min_y < 0:
            ay1 = ay1 - min_y
            ay2 = ay2 - min_y
            by1 = by1 - min_y
            by2 = by2 - min_y
        min_a_y = min([ay1, ay2])
        max_a_y = max([ay1, ay2])
        min_b_y = min([by1, by2])
        max_b_y = max([by1, by2])
        min_a_x = min([ax1, ax2])
        max_a_x = max([ax1, ax2])
        min_b_x = min([bx1, bx2])
        max_b_x = max([bx1, bx2])
        over_lapp_x = 0
        over_lapp_y = 0
        if max_b_y < max_a_y:
            if max_b_y < min_a_y:
                over_lapp_y = 0
            else:
                over_lapp_y = max_b_y - min_a_y
                ## adjust residual
                if min_a_y < min_b_y:
                    over_lapp_y = over_lapp_y - (min_b_y - min_a_y)
        else:
            if max_a_y < min_b_y:
                over_lapp_y = 0
            else:
                over_lapp_y = max_a_y - min_b_y
                if min_b_y < min_a_y:
                    over_lapp_y = over_lapp_y - (min_a_y - min_b_y)
        if max_b_x < max_a_x:
            if max_b_x < min_a_x:
                over_lapp_x = 0
            else:
                over_lapp_x = max_a_x - min_b_x
                if min_a_x < min_b_x:
                    over_lapp_x = over_lapp_x - (min_b_x - min_a_x)
        else:
            if max_a_x < min_b_x:
                over_lapp_x = 0
            else:
                over_lapp_x = max_a_x - min_b_x
                if min_b_x < min_a_x:
                    over_lapp_x = over_lapp_x - (min_a_x - min_b_x)
        if ax1 - ax2 == 0 or ay1 - ay2 == 0 or bx1 - bx2 == 0 or by1 - by2 == 0:
            over_lapp_x = 0
            over_lapp_y = 0
        return (
            abs(ax1 - ax2) * abs(ay1 - ay2)
            + abs(bx1 - bx2) * abs(by1 - by2)
            - over_lapp_y * over_lapp_x
        )


solution = Solution()
# print(solution.computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))
# print(solution.computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2))
# print(solution.computeArea(ax1=0, ay1=0, ax2=0, ay2=0, bx1=-1, by1=-1, bx2=1, by2=1))
print(solution.computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-1, by1=-1, bx2=1, by2=1))
