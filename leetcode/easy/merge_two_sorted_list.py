# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur_merged = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur_merged.next = list1
                list1 = list1.next
            else:
                cur_merged.next = list2
                list2 = list2.next

            cur_merged = cur_merged.next

        if list1:
            cur_merged.next = list1
        elif list2:
            cur_merged.next = list2

        return dummy.next



sol = Solution()

l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))

print(sol.mergeTwoLists(l1, l2))

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

