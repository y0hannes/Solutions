# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        path = []
        if root:
            for child in root.children:
                path.extend(self.postorder(child))
            path.append(root.val)

        return path
