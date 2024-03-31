from typing import List


class Solution:
    # brute force approach O(N^2)
    # def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    #     result = 0
    #     for i in range(len(nums)):
    #         count = set([nums[i]])
    #         if len(count)==k:
    #             result+=1
    #         for j in range(i+1,len(nums)):
    #             num = nums[j]
    #             if num not in count:
    #                 count.add(num)
    #             if len(count) ==k:
    #                 result+=1
    #             elif len(count)>k:
    #                 break
    #     return result
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Using two pointers algorithm to solve this problem
        1- Move the second pointer to the fardest you can, keep increse the count when k meet the criterial
        2- Move the first pointer to the fardest possible, keep increase the count when k meet the criterial
        3- Finish when k createrial break and f_i == len(nums)
        """
        f_i = 0
        s_i = 0
        counter = {}
        result = 0
        while f_i < len(nums):
            num = nums[f_i]
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

            if len(counter) == k:
                result += 1
                temp_dic = counter.copy()
                temp_s_i = s_i
                while len(temp_dic) == k:
                    temp_num = nums[temp_s_i]
                    temp_dic[temp_num] -= 1
                    if temp_dic[temp_num] == 0:
                        break
                    else:
                        result += 1
                        temp_s_i += 1

            elif len(counter) > k:
                # start moving the second pointer
                f_i -= 1
                del counter[num]
                while len(counter) == k:
                    s_num = nums[s_i]
                    counter[s_num] -= 1
                    if counter[s_num] == 0:
                        del counter[s_num]
                    s_i += 1
            f_i += 1
        return result


soltuion = Solution()
print(soltuion.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
