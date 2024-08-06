"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode):
        results = []
        # calling the helper for code cleaning
        self.rightSideViewHelper(root, results)
        return results
    
    def rightSideViewHelper(self, root: TreeNode, results):
        if not root: return
        results.append(root.val)
        # if the right is None but left has value, look for the left side
        if root.left and not root.right:
            return self.rightSideViewHelper(root.left, results)
        # only look for the right side
        if root.right:
          return self.rightSideViewHelper(root.right, results)
