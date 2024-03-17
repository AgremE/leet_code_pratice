# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_result = []
        curr_node = head
        curr_val = curr_node.val
        temp_result.append(curr_val)
        duplicate_elem = []
        while curr_node.next:
            next_val = curr_node.next.val
            curr_node = curr_node.next
            if curr_val == next_val:
                duplicate_elem.append(curr_val)
                continue
            temp_result.append(next_val)
            curr_val = next_val
        temp_list_node = []
        temp_result = [x for x in temp_result if x not in duplicate_elem]
        if temp_result == []:
            return ListNode()
        for val in temp_result:
            temp_list_node.append(ListNode(val))
        for i in range(1, len(temp_list_node)):
            temp_list_node[i - 1].next = temp_list_node[i]
        return temp_list_node[0]


### Create the List node
node = ListNode(1)
list_val = [1, 1]
temp_list_node = []
for val in list_val:
    temp_list_node.append(ListNode(val))
for i in range(1, len(temp_list_node)):
    temp_list_node[i - 1].next = temp_list_node[i]
curr = temp_list_node[0]
test = Solution().deleteDuplicates(curr)
while True:
    print(test.val)
    test = test.next
    if test == None:
        break
