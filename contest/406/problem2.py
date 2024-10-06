from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_head = None
        while head:
            if head.val in nums:
                continue
            if not new_head:
                new_head = ListNode(head.val)
                temp_head = new_head
            else:
                temp_head.next = ListNode(head.val)
                temp_head = temp_head.next
        return new_head
