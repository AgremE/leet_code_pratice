import heapq
from typing import List
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        list_nums = [(a,b) for a,b in zip(nums1,nums2)]
        list_nums = sorted(list_nums,key=lambda x: x[1],reverse=True)
        top_k = [x[0] for x in list_nums[:k]]
        heapq.heapify(top_k)
        top_k_sum = sum(top_k)
        result = top_k_sum*list_nums[k-1][1]
        for i in range(k,len(nums2)):
            top_k_sum -= heapq.heappop(top_k)
            top_k_sum+=list_nums[i][0]
            heapq.heappush(top_k,list_nums[i][0])
            result = max(result,top_k_sum*list_nums[i][1])
        return result