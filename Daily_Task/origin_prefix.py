from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = []
        for i in range(len(pref) - 1, 0, -1):
            num = pref[i]
            result.insert(0, pref[i] ^ pref[i - 1])
        result.insert(0, pref[0])
        return result


solution = Solution()
print(solution.findArray([5, 2, 0, 3, 1]))
