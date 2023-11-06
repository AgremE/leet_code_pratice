from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handle odd
        next = head
        if head.next:
            next_even = head.next
        else:
            next_even = None
        while True:
            if next.next.next:
                next.next = next.next.next
                next = next.next
                if not next:
                    break
            else:
                break
        next.next = next_even
        return head


llist = ListNode()
llist.val = 1
llist.next = ListNode()
next = llist.next
next.val = 2
next.next = ListNode()
next = next.next
next.val = 3
next.next = ListNode()
next = next.next
next.val = 4
next.next = ListNode()
next = next.next
next.val = 5
next.next = ListNode()

solution = Solution()
print(solution.oddEvenList(llist))
