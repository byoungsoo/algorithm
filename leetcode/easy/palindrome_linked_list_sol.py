from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half_head = self._reverse_list(slow)
        p1 = head
        p2 = second_half_head
        is_palindrome = True
        while p2:  # 뒤집힌 두 번째 절반이 끝날 때까지 비교 (p1이 먼저 끝날 수 있음)
            if p1.val != p2.val:
                is_palindrome = False
                break
            p1 = p1.next
            p2 = p2.next

        return True

    def _reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev  # 뒤집힌 리스트의 새로운 헤드


sol = Solution()
l1 = ListNode(1, ListNode(4, ListNode(3, ListNode(1, None))))
l2 = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(5, ListNode(4, ListNode(4, ListNode(1, None))))))))
l3 = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(1, None)))))))
result = sol.isPalindrome(l2)
print(result)

# Follow up: Could you do it in O(n) time and O(1) space?