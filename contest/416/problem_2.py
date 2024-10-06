from typing import List
import heapq 
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        best_cost = []
        time_tracker = [0 for _ in range(len(workerTimes))]
        heapq.heapify(best_cost)
        for i , w_t in enumerate(workerTimes):
            heapq.heappush(best_cost,(w_t,w_t,1,i))
        while mountainHeight >0:
            wt_ind, b_c, _mul, work_ind = heapq.heappop(best_cost)
            mountainHeight-=1
            time_tracker[work_ind]+=b_c
            _mul+=1 
            b_c  = workerTimes[work_ind]*(_mul)
            heapq.heappush(best_cost,(b_c+time_tracker[work_ind],b_c,_mul,work_ind))
        return max(time_tracker)

solution = Solution()
print(solution.minNumberOfSeconds(mountainHeight = 5, workerTimes = [1,5]))