import collections
from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        counter_num1 = collections.Counter(nums1)
        counter_num2 = collections.Counter(nums2)
        num1_remove = len(nums1) // 2
        num2_remove = len(nums2) // 2

        for num, _count in counter_num1.items():
            num1_remove = num1_remove - (_count - 1)
            counter_num1[num] = 1
            if num1_remove <= 0:
                break

        for num, _count in counter_num2.items():
            num2_remove = num2_remove - (_count - 1)
            counter_num2[num] = 1
            if num2_remove <= 0:
                break
        counter_num1_key = list(counter_num1.keys())
        counter_num2_key = list(counter_num1.keys())
        common_key = [x for x in counter_num1_key if x in counter_num2_key]
        left_one = 0
        left_two = 0
        if num1_remove > len(common_key):
            left_one = len(counter_num1_key) - (num1_remove - len(common_key))
