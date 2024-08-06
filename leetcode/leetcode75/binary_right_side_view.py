"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right # Definition for a binary tree node.

class Solution:
    def rightSideView(self, root: TreeNode):
        results = []
        # calling the helper for code cleaning
        results = self.rightSideViewHelper(root, results)
        return results
    
    def rightSideViewHelper(self, root: TreeNode, results):
        if not root:
            return []
    
        # Initialize a queue using deque for efficient pop from the front
        queue = deque([root])
        # List to store the order of visited nodes
        result = []
    
        while queue:
            right_side = None
            qLen = len(queue)

            # Loop by layers
            for i in range(qLen):
                # Pop the node from the front of the queue
                current_node = queue.popleft()

                if current_node:
                    # Append the current node's value to the result list
                    right_side = current_node

                    # If the current node has a left child, add it to the queue
                    if current_node.left:
                        queue.append(current_node.left)

                    # If the current node has a right child, add it to the queue
                    if current_node.right:
                        queue.append(current_node.right)
            if right_side:
                result.append(right_side.val)
        return result
