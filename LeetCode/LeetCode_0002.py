"""
2. Add Two Numbers (medium)

1) use stack
2) store value in node first, link the nodes later

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        nodes = []
        adds = 0
        while l1 is not None or l2 is not None or adds != 0:
            temp = ListNode()
            if l1 is not None:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0

            if l2 is not None:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            sums = l1_val + l2_val + adds
            if sums > 9:
                temp.val = sums - 10
                adds = 1
            else:
                temp.val = sums
                adds = 0
            nodes.append(temp)
        if len(nodes) == 1:
            return nodes[0]
        else:
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
        return nodes[0]