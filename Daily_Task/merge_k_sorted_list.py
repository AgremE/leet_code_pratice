# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from heapq import heapify, heappop,heappush
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        heapify(heap)
        for i in range(len(lists)):
            heappush(heap,(lists[i].val,i))
        result = ListNode()
        next = result
        while heap:
            next.next = ListNode()
            val,list_index = heappop(heap)
            next.val = val
            next = next.next
            lists[list_index] = lists[list_index].next
            if  lists[list_index]:
                heappush(heap,(lists[list_index].val,list_index))
        return result

