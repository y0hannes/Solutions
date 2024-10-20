# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = ListNode()
        temp.next = head
        last = temp

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            last = last.next
        
        last.next = last.next.next
        return temp.next