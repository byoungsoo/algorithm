# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
#
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return head

        dummy=ListNode(-101)
        cur = dummy

        cur.next = head
        while head:
            if head.val == cur.val:
                head = head.next
            else:
                cur.next = head
                cur = cur.next

        if head is None:
            cur.next = None

        return dummy.next

sol = Solution()

# h1 = ListNode(1, ListNode(1, ListNode(2, None)))
# h1 = ListNode(0, ListNode(0, ListNode(3, None)))
h1 = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(3, ListNode(3, None))))))))
result = sol.deleteDuplicates(h1)

while result:
    print(result.val)
    result=result.next

# Output: [1,2]


# Output: [1,2,3]