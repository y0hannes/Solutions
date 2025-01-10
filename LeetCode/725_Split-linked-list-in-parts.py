# https://leetcode.com/problems/split-linked-list-in-parts/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        curr = head
        ans = []
        
        size = count // k
        extra = count % k
        for i in range(k):
            top = curr
            amount = size + (1 if i < extra else 0)
            for _ in range(amount - 1):
                if curr:
                    curr = curr.next
            if curr:
                nx = curr.next
                curr.next = None
                curr = nx
            
            ans.append(top)
        return ans
