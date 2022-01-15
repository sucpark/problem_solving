"""
113. Path Sum II (Medium)

Description

Use Stack to solve the problem.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        stack = [(root, [])]
        sol = []

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                if sum(path) == targetSum - node.val:
                    path.append(node.val)
                    sol.append(path)
            else:
                path.append(node.val)
                if node.left:
                    stack.append((node.left, path.copy()))
                if node.right:
                    stack.append((node.right, path.copy()))

        return sol