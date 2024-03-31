from typing import Optional

"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # this should be linear algorithm
        # traverse through the list and count total node
        # travese through the list against with total node//2
        # make that last node point the the grand child node
        temp_head = head
        count = 0
        while temp_head:
            count += 1
            temp_head = temp_head.next
        if count == 1:
            return None
        del_node = count // 2
        temp_head = head
        for i in range(del_node - 1):
            temp_head = temp_head.next
        if temp_head.next:
            if temp_head.next.next:
                temp_head.next = temp_head.next.next
            else:
                temp_head.next = None
        return head
