from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = [x%k for x in arr]
        arr = sorted(arr)
        arr = [x for x in arr if x>0]
        if len(arr)%2!=0:
            return False
        for i in range(len(arr)//2):
            if (arr[i]+arr[len(arr)-1-i])%k!=0:
                return False
        return True

solution = Solution()
print(solution.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5))
print(solution.canArrange([1,2,3,4,5,6], k = 10))
print(solution.canArrange(arr = [1,2,3,4,5,6], k = 7))
