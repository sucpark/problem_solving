"""
783. Minimum Distance Between BST Nodes (easy)

1) Sort nodes in BST
2) Update minimal difference

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        node_list = []
        node_diff = sys.maxsize

        def add_node(node):
            if node.left is not None:
                add_node(node.left)
            node_list.append(node.val)
            if node.right is not None:
                add_node(node.right)

        add_node(root)

        for i in range(1, len(node_list)):
            node_diff = min(node_diff, node_list[i] - node_list[i - 1])
            if node_diff == 1:
                return node_diff
        return node_diff