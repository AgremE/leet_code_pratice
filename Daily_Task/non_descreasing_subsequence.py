from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ### Constructive again
        result = []
        arealdy_add = {}
        for i in range(len(nums)):
            num_i = nums[i]
            temp_result = []
            for j in range(len(result)):
                test = result[j].copy()
                if num_i >= test[len(test) - 1]:
                    test.append(num_i)
                    test_str = "".join([str(x) for x in test])
                    if test_str in arealdy_add:
                        continue
                    arealdy_add[test_str] = 1
                    temp_result.append(test)
            result = result + temp_result
            result.append([nums[i]])
        result = [x for x in result if len(x) > 1]
        return result


solution = Solution()
print(solution.findSubsequences(nums=[4, 6, 7, 7]))
