from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev_p = head
        cur_p = prev_p.next
        while cur_p:
            next_p = cur_p.next
            cur_p.next = prev_p
            prev_p = cur_p
            cur_p = next_p
        head.next = None
        return prev_p


sol = Solution()
h1 = ListNode(1, ListNode(2, ListNode(3, None)))
result = sol.reverseList(h1)

while result:
    print(result.val)
    result = result.next