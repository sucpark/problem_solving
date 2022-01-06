"""
501. Find Mode in Binary Search Tree (Easy)

Description

Firstly, I find all node values using DFS algorithm, especially inorder traversal.
After that, I use Counter function to find the frequency of elements in the array.
Then, I can find the maximum value in the Counter object.
Finally, using for-loop, I check every element which has the same frequency with the maximum value.
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


from collections import Counter


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        node_cnt = Counter(inorder(root))
        max_value = max(node_cnt.values())
        sol = []

        for i, v in node_cnt.items():
            if v == max_value:
                sol.append(i)

        return sol