"""
145. Binary Tree Postorder Traversal (Easy)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorder(node):
    if node:
        return postorder(node.left) + postorder(node.right) + [node.val]
    else:
        return []


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return postorder(root)