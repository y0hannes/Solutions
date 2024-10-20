# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr = ListNode()
        temp = curr 

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next if list1 else None
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next if list2 else None
            curr = curr.next
        
        while list1:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next if list1 else None
        
        while list2:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next if list2 else None
            
        return temp.next

        