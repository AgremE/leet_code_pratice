from typing import List


from collections import deque
import heapq


# class Solution:
#     """
#     This solution work but tooo slow
#     """
#     def survivedRobotsHealths(
#         self, positions: List[int], healths: List[int], directions: str
#     ) -> List[int]:
#         l_list = []
#         r_list = []
#         for i in range(len(healths)):
#             if directions[i] == "R":
#                 l_list.append([-positions[i], [healths[i], i]])
#             else:
#                 r_list.append([positions[i], [healths[i], i]])
#         heapq.heapify(l_list)
#         heapq.heapify(r_list)
#         result = []
#         while l_list:
#             pos_l, health_ind_l = heapq.heappop(l_list)
#             added_back_r = []
#             while r_list:
#                 po_r, health_ind_r = heapq.heappop(r_list)
#                 if abs(pos_l) > abs(po_r):
#                     added_back_r.append([po_r, health_ind_r])
#                     continue
#                 if health_ind_r[0] < health_ind_l[0]:
#                     health_ind_l[0] -= 1
#                 elif health_ind_r[0] == health_ind_l[0]:
#                     health_ind_l[0] = 0
#                     break
#                 else:
#                     health_ind_r[0] -= 1
#                     health_ind_l[0]  = 0
#                     added_back_r.append([po_r, health_ind_r])
#                     break
#             if health_ind_l[0] != 0:
#                 result.append(health_ind_l)
#             for elem in added_back_r:
#                 heapq.heappush(r_list, elem)
#         while r_list:
#             result.append(heapq.heappop(r_list)[1])
#         result = sorted(result, key=lambda x: x[1])
#         return [x[0] for x in result]


class Solution:
    """
    Maybe we could use stack instead
    """

    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        l_dir = deque([])
        r_dir = deque([])
        for i in range(len(healths)):
            if directions[i] == "L":
                l_dir.append([positions[i], healths[i], i])
            else:
                r_dir.append([positions[i], healths[i], i])
        l_dir = sorted(l_dir, key=lambda x: x[0], reverse=True)
        r_dir = sorted(r_dir, key=lambda x: x[0])
        result = []
        while l_dir:
            pos_l, health_l, ind_l = l_dir.pop()
            add_back = deque([])
            while r_dir:
                pos_r, health_r, ind_r = r_dir.pop()
                if pos_l < pos_r:
                    add_back.appendleft([pos_r, health_r, ind_r])
                else:
                    if health_r > health_l:
                        health_r -= 1
                        health_l = -1
                        add_back.appendleft([pos_r, health_r, ind_r])
                        break
                    elif health_r == health_l:
                        health_l = -1
                        break
                    else:
                        health_l -= 1
            if health_l != -1:
                result.append([health_l, ind_l])
            r_dir.extend(add_back)
        for elem in r_dir:
            result.append([elem[1], elem[2]])
        result = sorted(result, key=lambda x: x[1])
        return [x[0] for x in result]


soltuion = Solution()
print(soltuion.survivedRobotsHealths([5, 61, 98, 82], [180, 104, 8, 965], "RLLR"))
