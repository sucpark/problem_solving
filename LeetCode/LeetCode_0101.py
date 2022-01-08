"""
101. Symmetric Tree (Easy)

Description

We can solve this problem via two ways.
The first way is using recursive traversal.
If the tree is a mirror of itself, the result of preorder traversal for the left side
and the result of postorder traversal for the right side will be the same.
Since we want to clarify Null node, add outrange number, -101

The second way is using stack to impelemnt DFS algorithm.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def preorder(node):
            if node:
                return [node.val] + preorder(node.left) + preorder(node.right)
            else:
                return [-101]

        def postorder(node):
            if node:
                return postorder(node.left) + postorder(node.right) + [node.val]
            else:
                return [-101]

        if not root:
            return True

        left = preorder(root.left)
        right = postorder(root.right)

        return left == right[::-1]

        # if not root:
        #     return True
        #
        # stack = [(root.left, root.right)]
        # while stack:
        #     left, right = stack.pop()
        #
        #     if not left and not right:
        #         continue
        #     elif None in [left, right]:
        #         return False
        #     else:
        #         if left.val != right.val:
        #             return False
        #         stack.append((left.right, right.left))
        #         stack.append((left.left, right.right))
        #
        # return True
