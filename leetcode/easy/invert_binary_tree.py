from operator import invert
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root


sol = Solution()

t1 =TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(7, TreeNode(6, None, None), TreeNode(9, None, None)))
t2 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
t4 = None

result = sol.invertTree(t1)
print(result)

