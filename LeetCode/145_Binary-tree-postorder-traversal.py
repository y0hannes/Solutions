# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._post(root, [])
    def _post(self, root, path):
        if root:
            self._post(root.left, path)
            self._post(root.right, path)
            path.append(root.val)
        return path
        