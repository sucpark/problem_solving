"""
230. Kth Smallest Element in a BST (Medium)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(node):
    if node:
        return inorder(node.left) + [node.val] + inorder(node.right)
    else:
        return []


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sol = inorder(root)
        return sol[k - 1]