# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

#the edge case where head does not exist
        while curr:
            holder = curr.next
            curr.next = prev
            prev = curr
            curr = holder
        return prev