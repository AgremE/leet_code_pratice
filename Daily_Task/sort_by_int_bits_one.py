from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_count_one(num):
            count_one = 0
            for i in range(16, 0, -1):
                if num >= 2**i:
                    count_one = count_one + 1
                    _div = num % 2**i
                    if (_div == 1) & (num % 2**i == 0):
                        num = 0
                        break
                    num = _div
            if num == 1:
                count_one = count_one + 1
            return count_one

        result_count = []
        for num in arr:
            result_count.append((num, get_count_one(num) * 10**5 + num))
        result_count.sort(key=lambda x: x[1])
        return [x[0] for x in result_count]


solution = Solution()
print(solution.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(solution.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
