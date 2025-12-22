from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None

        p1 = head
        dummy = ListNode()
        dummy.next = p1
        p2 = dummy
        while p1:
            if p1.val == val:
                p1 = p1.next
                p2.next = p1
            else:
                p2 = p1
                p1 = p1.next
        return dummy.next





sol = Solution()
h1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))
h2 = None
h3 = ListNode(7 , ListNode(7 , ListNode(7 , ListNode(7 , None))))


result = sol.removeElements(h1, 6)

while result:
    print(result.val)
    result = result.next