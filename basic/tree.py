from collections import deque
from contextlib import nullcontext


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 예시 트리 구성
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
root = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, None, TreeNode(6))
               )

# tree3 = TreeNode(0, TreeNode(-3, TreeNode(-10, None, None), None), TreeNode(9, TreeNode(5, None, None), None))


# 전위 순회 (재귀) -> 리스트 반환
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# 후위 순회 (재귀) -> 리스트 반환
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def level_order(root):
    if root is None:
        return []
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res
# 예시 트리 구성
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# result = preorder(tree3)
# print(result)
#
# result = inorder(tree3)
# print(result)
#
# result = postorder(tree3)
# print(result)

result = level_order(root)
print(result)