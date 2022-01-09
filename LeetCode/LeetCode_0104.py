"""
104. Maximum Depth of Binary Tree (Easy)

Description

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        level = [root]
        cnt = 0

        while level:
            cnt += 1
            curr_level_node = []
            for e in level:
                if e.left:
                    curr_level_node.append(e.left)
                if e.right:
                    curr_level_node.append(e.right)
            level = curr_level_node

        return cnt