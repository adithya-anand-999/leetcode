# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#we make a new ListNode() and both dummy and curr point to the same thing
        dummy = curr = ListNode()
        # dummy = ListNode()
        # curr = ListNode()
        # dummy.next = curr
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            #moving curr here builds the list 
            curr = curr.next
        if list1: curr.next = list1
        else: curr.next = list2
        return dummy.next
        