"""
1290. Convert Binary Number in a Linked List to Integer (easy)

1) linked list problem

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = []
        sol = 0

        while head is not None:
            temp.append(head.val)
            head = head.next

        for i, v in enumerate(temp[::-1]):
            sol += v * (2 ** i)

        return sol