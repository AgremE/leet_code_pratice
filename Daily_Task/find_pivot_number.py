class Solution:
    def pivotInteger(self, n: int) -> int:
        result = (n*(n+1)/2)**0.5
        if int(result)==result:
            return result
        return -1 

solution = Solution()
print(solution.pivotInteger(8))