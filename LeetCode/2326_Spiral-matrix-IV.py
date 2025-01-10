# https://leetcode.com/problems/spiral-matrix-iv/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [[-1] * n for _ in range(m)]

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while head:
            for j in range(left, right + 1):
                if not head:
                    break
                matrix[top][j] = head.val
                head = head.next
            top += 1
            for j in range(top, bottom + 1):
                if not head:
                    break
                matrix[j][right] = head.val
                head = head.next
            right -= 1
            for j in range(right, left - 1, -1):
                if not head:
                    break
                matrix[bottom][j] = head.val
                head = head.next
            bottom -= 1
            for j in range(bottom, top  - 1, -1):
                if not head:
                    break
                matrix[j][left] = head.val
                head = head.next
            left += 1
            # if bottom < top and right < left:
            #     return
        return matrix