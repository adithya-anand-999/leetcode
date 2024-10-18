# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1: cur.next = list1
        #you can do else here because we are only modifying one list at a time, this means even if the lists are of the same length we exit the while loop with one loop still having remaining nodes. So we only have to check on, then can safley add the other. Both can never be true as then the while loop will continue iterating. 
        else: cur.next = list2
        return dummy.next