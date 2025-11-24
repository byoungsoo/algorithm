# Given the root of a binary tree, return the inorder traversal of its nodes' values.
from typing import Optional


# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)




sol = Solution()

tree = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
tree1 = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, TreeNode(6, None, None), TreeNode(7, None, None))), TreeNode(3, None, TreeNode(8, TreeNode(9, None, None), None)))
tree2 = TreeNode(1, None, None)


result = sol. inorderTraversal(tree2)
print(result)