"""
19. Remove Nth Node From End of List (Medium)

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        head_list = []
        while head:
            head_list.append(head)
            head = head.next

        target_node_idx = len(head_list) - n
        if target_node_idx == 0:
            head = head_list[target_node_idx].next
        else:
            head_list[target_node_idx - 1].next = head_list[target_node_idx].next
            head = head_list[0]
        return head