# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        mapping = {}
        while head:
            if head in mapping:
                return True
            else:
                mapping[head] = head.val
                head = head.next
        return False
