from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)
            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            print(f"left_height: {left_height}")
            print(f"right_height: {right_height}")

            return [is_balanced, 1 + max(left_height, right_height)]

        return dfs(root)[0]



sol = Solution()

t1 = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
t2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, None, None), TreeNode(4, None, None)), TreeNode(3, None, None)), TreeNode(2, None, None))
t3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, None)))
t4 = TreeNode(1, None, None)

result = sol.isBalanced(t4)
print(result)