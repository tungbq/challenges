"""
Problem: Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        # print(min(left_depth, right_depth) + 1)
        return min(left_depth, right_depth) + 1

# Test case for the solution
def test_min_depth():
    # Create the binary tree [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    solution = Solution()
    assert solution.minDepth(root) == 2, "Test case 1 failed!"

    # Another test case: [1, None, 2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    
    assert solution.minDepth(root) == 2, "Test case 2 failed!"

    # Test case with empty tree
    root = None
    
    assert solution.minDepth(root) == 0, "Test case 3 failed!"


  # More complex test case
    # Tree: [2, 3, 4, 5, None, None, 6, None, 7]
    # .....2
    # ...3...4...
    # ..5....6...    
    # .7.....
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.right = TreeNode(7)
    
    assert solution.minDepth(root) == 3, "Test case 4 failed!"

    # Another complex test case
    # Tree: [1, 2, None, 3, None, 4, None, 5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    
    assert solution.minDepth(root) == 5, "Test case 5 failed!"

    # Tree with varying depths
    # Tree: [1, 2, 3, 4, None, None, 5, 6, None, None, 7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    
    assert solution.minDepth(root) == 4, "Test case 6 failed!"

    print("All test cases passed!")

# Run the test case
test_min_depth()
