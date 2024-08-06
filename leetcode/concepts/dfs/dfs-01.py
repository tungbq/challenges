# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

# Test case for the solution
def test_max_depth():
    # Create the binary tree [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    solution = Solution()
    assert solution.maxDepth(root) == 3, "Test case failed!"

    # Another test case: [1, None, 2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    
    assert solution.maxDepth(root) == 2, "Test case failed!"

    # Test case with empty tree
    root = None
    
    assert solution.maxDepth(root) == 0, "Test case failed!"

    print("All test cases passed!")

# Run the test case
test_max_depth()
