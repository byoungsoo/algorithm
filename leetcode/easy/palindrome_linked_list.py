from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        list_val = []
        while head:
            list_val.append(head.val)
            head = head.next

        p1 = 0
        p2 = len(list_val)-1
        while p1 <= p2:
            if list_val[p1] != list_val[p2]:
                return False
            p1 +=1
            p2 -=1
        return True


sol = Solution()
l1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
l2 = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(1, None)))))))
result = sol.isPalindrome(l2)
print(result)

# Follow up: Could you do it in O(n) time and O(1) space?