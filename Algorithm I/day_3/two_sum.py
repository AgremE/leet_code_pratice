class Solution:
    def twoSum(self, numbers, target):
        l_ind = 0
        r_ind = len(numbers) - 1
        result = []
        while l_ind < r_ind:
            print(r_ind)
            if target < numbers[l_ind] + numbers[r_ind]:
                r_ind = r_ind - 1
            elif target > numbers[l_ind] + numbers[r_ind]:
                l_ind = l_ind + 1
            else:
                return [l_ind+1,r_ind+1]
        return result

test_solution = Solution()
print(test_solution.twoSum([2,7,11,15],9))