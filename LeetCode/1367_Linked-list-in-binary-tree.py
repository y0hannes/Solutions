# https://leetcode.com/problems/linked-list-in-binary-tree/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def fun(head: ListNode, root : TreeNode):
            if not head:
                return True
            if not root or root.val != head.val:
                return False

            return fun(head.next, root.left) or fun(head.next, root.right)
        
        if not root:
            return False
        if fun(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)