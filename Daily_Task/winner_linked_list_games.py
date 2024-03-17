# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def gameResult(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: str
        """
        odd_win = 0
        even_win = 0
        is_even_node = True
        while head:
            if head.val > head.next.val:
                even_win += 1
                head = head.next.next
            else:
                odd_win += 1
                head = head.next.next
        if odd_win > even_win:
            return "Odd"
        elif even_win > odd_win:
            return "Even"
        else:
            return "Tie"
