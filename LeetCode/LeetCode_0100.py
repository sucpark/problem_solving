"""
100. Same Tree (Easy)

Description

The First solution is using DFS algorithm via stack.
After putting a pair of node set into the stack, check it the validation from the top/
If two nodes are both None, we should pass the case.
If the only one of the node is None, then we know it is False case.
If two nodes are not None but the values are different with each other, then it is wrong.
Lastly, we can add left node pairs and right nodes pairs to the stack.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#         stack = [(p, q)]

#         while stack:
#             node1, node2 = stack.pop()

#             if not node1 and not node2:
#                 continue
#             elif None in [node1, node2]:
#                 return False
#             else:
#                 if node1.val != node2.val:
#                     return False
#                 else:
#                     stack.append((node1.right, node2.right))
#                     stack.append((node1.left, node2.left))
#         return True
