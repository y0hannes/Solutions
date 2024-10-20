# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._traversal(root, [])

    def _traversal(self, root, path):

        if root:
            self._traversal(root.left, path)
            path.append(root.val)
            self._traversal(root.right, path)
        return path