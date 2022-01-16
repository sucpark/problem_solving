"""
83. Remove Duplicates from Sorted List (Easy)

Description

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        post = head

        while curr:

            if post and curr.val == post.val:
                post = post.next
            else:
                curr.next = post
                curr = curr.next
        return head