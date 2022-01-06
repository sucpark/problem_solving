"""
98. Validate Binary Search Tree (Medium)

Description

I want to use DFS algorithm to solve the problem.
We know that in-order traversal makes ascending array for binary search tree.
Thus, after in-order traversal, if the array is not ascending, we can determine that it is not a BST.
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        nodes = inorder(root)

        for i in range(1, len(nodes)):
            if nodes[i - 1] >= nodes[i]:
                return False

        return True