"""
Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        # Initialize an empty list to store the inorder traversal result
        result = []
        # Start the recursive inorder traversal
        self._inorder_helper(root, result)
        # Return the final result
        return result
    
    def _inorder_helper(self, node: TreeNode, result: list):
        # Base case: if the current node is None, return
        if not node:
            return
        # Recursively traverse the left subtree
        self._inorder_helper(node.left, result)
        # Visit the current node and add its value to the result list
        result.append(node.val)
        # Recursively traverse the right subtree
        self._inorder_helper(node.right, result)

# Test cases for the solution
def test_inorder_traversal():
    # Test case 1: Tree [1, None, 2, 3]
    # Tree structure:
    #    1
    #     \
    #      2
    #     /
    #    3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    solution = Solution()
    assert solution.inorderTraversal(root) == [1, 3, 2], "Test case 1 failed!"

    # Test case 2: Empty tree
    root = None
    
    assert solution.inorderTraversal(root) == [], "Test case 2 failed!"

    # Test case 3: Tree [1]
    # Tree structure:
    #    1
    root = TreeNode(1)
    
    assert solution.inorderTraversal(root) == [1], "Test case 3 failed!"

    # Test case 4: More complex tree [2, 3, 4, 5, None, None, 6, None, 7]
    # Tree structure:
    #         2
    #       /   \
    #      3     4
    #     /       \
    #    5         6
    #     \
    #      7
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.right = TreeNode(7)
    
    assert solution.inorderTraversal(root) == [5, 7, 3, 2, 4, 6], "Test case 4 failed!"

    # Test case 5: Tree with a single left-leaning branch [1, 2, None, 3, None, 4, None, 5]
    # Tree structure:
    #    1
    #   /
    #  2
    # /
    # 3
    # /
    # 4
    # /
    # 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    
    assert solution.inorderTraversal(root) == [5, 4, 3, 2, 1], "Test case 5 failed!"

    print("All test cases passed!")

# Run the test cases
test_inorder_traversal()
