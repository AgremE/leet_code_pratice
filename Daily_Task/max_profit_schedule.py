from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        def bundle_job(startTime, endTime, profit):
            result = []
            for i in range(len(startTime)):
                result.append([startTime[i], endTime[i], profit[i]])
            return sorted(result, key=lambda x: x[0])

        def recurv(info, s_i, memoir):
            if s_i in memoir:
                return memoir[s_i]
            if s_i >= len(startTime):
                return 0
            memoir[s_i] = max(
                [recurv(info, s_i, memoir) + info[s_i][2], recurv(info, s_i, memoir)]
            )
            return memoir[s_i]

        memoir = {}
        result = []
        info = bundle_job(startTime, endTime, profit)
        # for i in range(len(startTime)):
        #     result.append(recurv(info, i, memoir))
        return recurv(info, 0, memoir)
        return max(result)


solution = Solution()
# print(solution.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
print(solution.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))
