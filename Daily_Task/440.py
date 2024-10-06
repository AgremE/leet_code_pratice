class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        max_len= 0
        while max_len<10:
            test = n//(10**max_len)
            if test == 0:
                break
            max_len+=1
        max_len-=1
        ind_sorted = [[] for _ in range(10**(max_len+1))]
        for i in range(1,n):
            k = 0
            while k<10:
                if i % (10**k)==0:
                    k+=1
                else:
                    k-=1
                    break
            leading = (i//(10**k))*(10**(max_len-k-1))
            ind_sorted[leading].append(i)
        ind = 0
        while k != 0:
            if len(ind_sorted[ind])>k:
                return ind_sorted[ind][k]
            else:
                k-=len(ind_sorted[ind])

solution = Solution()
print(solution.findKthNumber(n = 13, k = 2))