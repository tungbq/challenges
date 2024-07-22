"""
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def maxDepth(self, node, depth=0, maxdepth=0) -> int:
      if not node:
        return 0
      print(node.val)  # Process the node
      max_child = max(self.maxDepth(node.left, depth, maxdepth), self.maxDepth(node.right, depth, maxdepth)) + 1
      return max_child

root_list = [3,9,20,None,None,15,7]
root = list_to_tree(root_list)


sol = Solution()
maxDepth = sol.maxDepth(root)
print("maxDepth:")
print(maxDepth)
