"""
206. Reverse Linked List (easy)

1) define the current node and check the next node
2) convert the current node's next to prev node
3) set the prev node  as the current node and current node as next node

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        return prev

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         if head is None:
#             return head
#
#         sol = ListNode(val=head.val)
#         head = head.next
#
#         while head:
#             temp = ListNode(val=head.val, next=sol)
#             sol = temp
#             head = head.next
#         return sol