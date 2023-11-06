from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2 * k + 1:
            return [-1 for x in range(len(nums))]
        if k == 0:
            return nums
        nums = [float(x) for x in nums]
        s_ind = k
        s_val = nums[0]
        e_val = nums[2 * k]
        total_sum = sum(nums[: 2 * k + 1])
        num_itterate = len(nums) - (2 * k + 1)
        result = [total_sum // (2 * k + 1)]
        for i in range(1, num_itterate + 1):
            next_s = nums[i]
            next_e = nums[2 * k + i]
            total_sum = total_sum - s_val + next_e
            s_val = next_s
            e_val = next_e
            result.append(total_sum // (2 * k + 1))
        result = (
            [-1 for i in range(k)] + [int(x) for x in result] + [-1 for i in range(k)]
        )
        return result


solution = Solution()
print(
    solution.getAverages(
        nums=[
            6643,
            3914,
            1918,
            9122,
            3503,
            4072,
            8633,
            5893,
            952,
            4377,
            1052,
            4513,
            3157,
            9894,
            9102,
            8734,
            9068,
            2121,
            4098,
            5039,
            5698,
            5224,
            2797,
            5440,
            1541,
            9419,
            9475,
            4465,
            5490,
            159,
            829,
            5701,
            314,
        ],
        k=5,
    )
)
