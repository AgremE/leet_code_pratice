from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
         def is_overlap(point_a,point_b):
             x_s_1, x_e_1 = point_a
             x_s_2, x_e_2 = point_b
             ### Check if a in b or b in a
             if ((x_s_2 <= x_s_1)and(x_e_1 <= x_e_2)) or ((x_s_1 <= x_s_2)and(x_e_2 <= x_e_1):
                 return True
            else:
                ## Check if a partially part b in the start or vice versa
                if (())
            
            return False