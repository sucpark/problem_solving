"""
112. Path Sum (Easy)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder(node, val, target):
    if node:
        val += node.val

        if node.left or node.right:
            return preorder(node.left, val, target) or preorder(node.right, val, target)
        else:
            if val == target:
                return True
            else:
                return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return preorder(root, 0, targetSum)