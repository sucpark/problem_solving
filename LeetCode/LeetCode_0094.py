"""
94. Binary Tree Inorder Traversal (Easy)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder(node):
    if node:
        return [node.val] + preorder(node.left) + preorder(node.right)
    else:
        return []


def inorder(node):
    if node:
        return inorder(node.left) + [node.val] + inorder(node.right)
    else:
        return []


def postorder(node):
    if node:
        return postorder(node.left) + postorder(node.right) + [node.val]
    else:
        return []


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return inorder(root)