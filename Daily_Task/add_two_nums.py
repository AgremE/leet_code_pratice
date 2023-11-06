# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first_num = ""
        second_num = ""
        while l1:
            first_num = first_num + str(l1.val)
            l1 = l1.next
        while l2:
            second_num = second_num + str(l2.val)
            l2 = l2.next
        first_num = int(first_num[::-1])
        second_num = int(second_num[::-1])
        result = first_num + second_num
        result = str(result)[::-1]
        node = ListNode()
        temp_node = node
        for i in range(len(result)):
            temp_node.val = result[i]
            if i == len(result) - 1:
                continue
            temp_node.next = ListNode()
            temp_node = temp_node.next
        return node


###
solution = Solution()
l1 = ListNode()
temp_node = l1
l1_num = [0, 8, 6, 5, 6, 8, 3, 5, 7]
for i in range(len(l1_num)):
    num = l1_num[i]
    temp_node.val = num
    if i == len(l1_num) - 1:
        continue
    temp_node.next = ListNode()
    temp_node = temp_node.next

l2 = ListNode()
temp_node = l2
l2_num = [6, 7, 8, 0, 8, 5, 8, 9, 7]
for i in range(len(l2_num)):
    num = l2_num[i]
    temp_node.val = num
    if i == len(l2_num) - 1:
        continue
    temp_node.next = ListNode()
    temp_node = temp_node.next

result = solution.addTwoNumbers(l1, l2)
print(result)
# while result:
#     print(result.val)
#     result = result.next
