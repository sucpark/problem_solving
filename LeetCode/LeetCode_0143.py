"""
143. Reorder List (Medium)

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return None

        # find the middle point of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow

        # reverse the half of the list
        prev, curr = None, mid
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two linked lists:
        first, second = head, prev
        while second.next:
            next_hop = first.next
            first.next = second
            first = next_hop

            next_hop = second.next
            second.next = first
            second = next_hop
