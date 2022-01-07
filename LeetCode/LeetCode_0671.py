"""
671. Second Minimum Node In a Binary Tree (Easy)

Description

Firstly, I want to get all node values in the binary tree using DFS algorithm.
Among the three types of DFS: pre-order, in-order, and post-order traversal, I use pre-order traversal.
The difference between the types is the visiting order of the center node.
We can choose any type of traversal because it is not a binary search tree.

After getting all node values, I check how many distinct values are there using set function.

Lastly, if there are more than two distinct values, we can find the second smallest value using sort function.
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        nodes = preorder(root)
        nodes = sorted(set(nodes))

        if len(nodes) == 1:
            return -1
        else:
            return nodes[1]