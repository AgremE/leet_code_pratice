from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        The algorithm is going as following:
        1- Using two pointer to find the longest subarray that have product less than k from any starting point s_i
        2- For each sub array, the total number of sub array is n(n+1)/2
        """
        count = 0
        s_i = 0
        f_i = 0
        product = 1
        total_len_count = []
        double_count = 0
        interval = []
        while s_i != len(nums):
            product *= nums[f_i]
            if f_i == len(nums) - 1:
                if product * nums[f_i] < k:
                    total_len_count.append(f_i - s_i + 1)
                    interval.append([s_i, f_i])
                    break
            if product < k:
                f_i += 1
                if f_i == len(nums) - 1:
                    if product * nums[f_i] < k:
                        total_len_count.append(f_i - s_i + 1)
                        interval.append([s_i, f_i])
                        break
            else:
                total_len_count.append(f_i - s_i)
                interval.append([s_i, f_i - 1])
                if f_i == s_i:
                    f_i += 1
                    s_i += 1
                    product = 1
                else:
                    product /= nums[s_i]
                    product /= nums[f_i]
                    s_i += 1
        total_len_count = [x for x in total_len_count if x != 0]
        result = 0
        if not total_len_count:
            return 0
        for count in total_len_count:
            result += count * (count + 1) // 2
        # count duplicated
        for i in range(1, len(interval)):
            if interval[i - 1][1] - interval[i][0] + 1 > 0:
                double_count += interval[i - 1][1] - interval[i][0] + 1

        return result - double_count


solution = Solution()
print(
    solution.numSubarrayProductLessThanK(
        [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19
    )
)
