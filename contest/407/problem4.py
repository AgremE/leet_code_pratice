from typing import List


### 100329
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diff = [x - y for x, y in zip(nums, target)]
        result = 0
        pre_sign = None
        temp = []

        def handle_last_op(list_num):
            x = [abs(x) for x in list_num]
            dis_join_i = []
            for i in range(1, len(x)):
                if x[i] <= x[i - 1] and x[i] <= x[i + 1]:
                    dis_join_i.append(i)

        for d in diff:
            if not pre_sign:
                if d != 0:
                    pre_sign = d
                    temp.append(d)
            else:
                if pre_sign > 0 and d < 0:
                    pre_sign = d
                    result += handle_last_op(temp)
                    temp = [d]
                elif pre_sign < 0 and d > 0:
                    pre_sign = d
                    result += handle_last_op(temp)
                    temp = [d]
                elif d == 0:
                    result += handle_last_op(temp)
                    temp = []
                else:
                    temp.append(d)

        result += max([abs(x) for x in temp])
        return result


solution = Solution()
# print(solution.minimumOperations(   nums = [3,5,1,2], target = [4,6,2,4]     ))
# print(solution.minimumOperations(  nums = [1,3,2], target = [2,1,4]))
print(
    solution.minimumOperations(
        nums=[9, 2, 6, 10, 4, 8, 3, 4, 2, 3], target=[9, 5, 5, 1, 7, 9, 8, 7, 6, 5]
    )
)
