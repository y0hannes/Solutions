# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        first = head
        second = first.next
        while second:
            temp = ListNode(math.gcd(first.val, second.val))
            first.next = temp
            temp.next = second
            first = second
            second = second.next
        return head
