from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        This should be able to use dynamic algo
        it is like a subsegment prblem
        """
        diff_map = []
        for i in range(len(arr)):
            temp_result = []
            for x in range(i + 1, len(arr)):
                temp_result.append(arr[x] - arr[i])
            diff_map.append(temp_result)
        memoir = {}

        def recurv_count(diff_map, diff_con, x, memoir):
            if x in memoir:
                return memoir
            if x >= len(diff_map):
                return 1
            for y in range(len(diff_map[x])):
                _diff = diff_map[x][y]
                temp_result = []
                if _diff == diff_con:
                    temp_result.append()
