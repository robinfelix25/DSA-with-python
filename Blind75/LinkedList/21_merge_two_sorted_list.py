
"""
coding in leetcode and copying here for reference
No time to insert it as linked list,
revisit
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head
        while list1 != None or list2 != None :
            # print(list1.val, list2.val)
            if list1 is None: 
                head.next = list2
                break
            if list2 is None: 
                head.next = list1
                break
            if list1.val <= list2.val:
                out = ListNode(val=list1.val)
                head.next = out
                head = out
                list1 = list1.next
            else:
                out = ListNode(val=list2.val)
                head.next = out
                head = out
                list2 = list2.next
        
        return dummy.next