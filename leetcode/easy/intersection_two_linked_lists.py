from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        pt_A = headA
        pt_B = headB

        while pt_A is not pt_B:
            pt_A = pt_A.next
            pt_B = pt_B.next
            if pt_A is None and pt_B is None:
                return None

            if pt_A is None:
                pt_A = headB
            if pt_B is None:
                pt_B = headA

        return pt_A

# Sol is
# headA-> A + C + B + C
# headB-> B + C + A + C
# Finally, no matter A and B have different size, they will get intersection point at last C
