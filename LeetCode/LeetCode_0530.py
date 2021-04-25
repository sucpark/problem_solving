"""
530. Minimum Absolute Difference in BST (easy)


1) BST search - sort nodes
2) Compare the difference
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:

        node_list = []
        node_diff = sys.maxsize

        def sort_node(node):
            if node.left is not None:
                sort_node(node.left)
            node_list.append(node.val)
            if node.right is not None:
                sort_node(node.right)

        sort_node(root)
        for i in range(1, len(node_list)):
            node_diff = min(node_diff, node_list[i] - node_list[i - 1])

        print(node_list)
        return node_diff