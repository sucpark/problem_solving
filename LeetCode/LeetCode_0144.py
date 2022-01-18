"""
144. Binary Tree Preorder Traversal (Easy)


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


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return preorder(root)