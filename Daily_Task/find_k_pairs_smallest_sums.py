from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        def get_possible_move(x, y, max_x, max_y):
            possible_move = []
            if x < max_x:
                possible_move.append((x + 1, y))
                if y < max_y:
                    possible_move.append((x + 1, y + 1))
            if x - 1 >= 0:
                possible_move.append((x - 1, y))
                if y - 1 >= 0:
                    possible_move.append((x - 1, y - 1))
            if y < max_y:
                possible_move.append((x, y + 1))
            if y - 1 >= 0:
                possible_move.append((x, y - 1))
            return possible_move

        sequence_heap = []
        heapq.heapify(sequence_heap)
        already_visite = {}
        step = (0, 0)
        total_sum = 0
        result = []
        len_num1 = len(nums1)
        len_num2 = len(nums2)
        for i in range(k):
            ##
            # Just use the min heap to for from (0,0) index part from num1 and num2
            # #
            result.append([nums1[step[0]], nums2[step[1]]])
            already_visite[f"n1{step[0]}_n2{step[1]}"] = True
            _moves = get_possible_move(step[0], step[1], len_num1 - 1, len_num2 - 1)
            print(f"n1{step[0]}_n2{step[1]}")
            for _m in _moves:
                _m_str = f"n1{_m[0]}_n2{_m[1]}"
                if _m_str in already_visite:
                    continue
                heapq.heappush(
                    sequence_heap, ((nums1[_m[0]] + nums2[_m[1]]), (_m[0], _m[1]))
                )
            ## get min score
            while len(sequence_heap) != 0:
                reward, step = heapq.heappop(sequence_heap)
                if not (f"n1{step[0]}_n2{step[1]}" in already_visite):
                    break

            if len(sequence_heap) == 0:
                return result
        return result


solution = Solution()
print(solution.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=10))
