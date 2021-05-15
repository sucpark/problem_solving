"""
111. Minimum Depth of Binary Tree (easy)

1) use DFS
2) check the visited node
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if (root.left is None) and (root.right is None):
            return 1

        stack = [root]
        depth = sys.maxsize
        while stack:
            curr = stack[-1]
            if (curr.left is None) and (curr.right is None):
                depth = min(depth, len(stack))
                stack.pop()
            elif (curr.left is not None) and (curr.left != 'visited'):
                stack.append(curr.left)
                curr.left = 'visited'
            elif (curr.right is not None) and (curr.right != 'visited'):
                stack.append(curr.right)
                curr.right = 'visited'
            else:
                stack.pop()
        return depth