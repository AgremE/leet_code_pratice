# Definition for singly-linked list.
from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        middle_node = head
        get_count_node = head
        count = 1
        while get_count_node.next:
            count += 1
            get_count_node = get_count_node.next
        middle_i = count // 2
        for _ in range(middle_i):
            middle_node = middle_node.next
        _max = -math.inf
        _start_val = []
        _end_val = []
        for _ in range(middle_i):
            _start_val.append(head.val)
            _end_val.append(middle_node.val)
            head = head.next
            middle_node = middle_node.next
        _end_val = _end_val[::-1]
        return max(x + y for x, y in zip(_start_val, _end_val))


head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

solution = Solution()
print(solution.pairSum(head))
