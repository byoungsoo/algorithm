from typing import Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[list['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        def dfs(root_node):
            if not root_node:
                return 0

            height_total = 0
            height_max = 0
            for cur in root_node.children:
                height_total = dfs(cur) + 1
                height_max = max(height_max, height_total)
            return height_max

        return dfs(root) + 1


n1 = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
n2 = Node(1, [Node(2, []), Node(3, [Node(6, []), Node(7, [Node(11, [Node(14, [])])])]), Node(4, [Node(8, [Node(12, [])])]), Node(5, [Node(9, [Node(13, [])]), Node(10, [])])])
n3 = None


sol = Solution()
result = sol.maxDepth(n3)
print(f"result= {result}")