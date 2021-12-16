"""
147. Insertion Sort List (Medium)

1) use two pointers : last sorted, current

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode(-5001, head)
        last_sorted = head
        curr = head.next

        while curr:
            if last_sorted.val < curr.val:
                last_sorted, curr = curr, curr.next
            else:
                prev = dummy_head
                while prev.next.val < curr.val:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = last_sorted.next
        return dummy_head.next