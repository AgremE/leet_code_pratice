class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [0 for _ in range(n)]
        ugly_nums[0] = 1

        ind_mul_2,ind_mul_3,ind_mul_5 =0,0,0
        mul_2,mul_3,mul_5 = 2,3,5

        for i in range(1,n):
            cur_min_mul = min(mul_2,mul_3,mul_5)
            ugly_nums[i] = cur_min_mul
            if cur_min_mul == mul_2:
                ind_mul_2+=1
                mul_2=ugly_nums[ind_mul_2]*2
            if cur_min_mul == mul_3:
                ind_mul_3+=1
                mul_3=ugly_nums[ind_mul_3]*3
            if cur_min_mul == mul_5:
                ind_mul_5+=1
                mul_5=ugly_nums[ind_mul_5]*5
        return ugly_nums[n-1]

solution = Solution()
print(solution.nthUglyNumber(10))