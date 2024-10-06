from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        next_val = 0
        while head:
            if head.val != 0:
                next_val += head.val
            else:
                if new_head:
                    temp_head.next = ListNode(val=next_val)
                    next_val = 0
                    temp_head = temp_head.next
                else:
                    new_head = ListNode(val=next_val)
                    temp_head = new_head
        temp_head.next = None
        return new_head
