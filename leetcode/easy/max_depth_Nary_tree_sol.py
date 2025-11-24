from typing import Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[list['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0
        if not root.children:
            return 1

        max_child_depth = 0

        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child) + 1)

        return max_child_depth


n1 = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
n2 = Node(1, [Node(2, []), Node(3, [Node(6, []), Node(7, [Node(11, [Node(14, [])])])]), Node(4, [Node(8, [Node(12, [])])]), Node(5, [Node(9, [Node(13, [])]), Node(10, [])])])
n3 = None


sol = Solution()
result = sol.maxDepth(n2)
print(f"result= {result}")