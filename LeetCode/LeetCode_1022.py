"""
1022. Sum of Root To Leaf Binary Numbers (Easy)

Description
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs_sum(node, total):
    if node is None:
        return 0
    else:
        total = 2 * total + node.val
        if not node.left and not node.right:
            return total
        else:
            return dfs_sum(node.left, total) + dfs_sum(node.right, total)


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return dfs_sum(root, 0)