# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        # Initialize an empty list to store the preorder traversal result
        result = []
        # Start the recursive preorder traversal
        self._preorder_helper(root, result)
        # Return the final result
        return result
    
    def _preorder_helper(self, node: TreeNode, result: list):
        # Base case: if the current node is None, return
        if not node:
            return
        # Visit the current node and add its value to the result list
        result.append(node.val)
        # Recursively traverse the left subtree
        self._preorder_helper(node.left, result)
        # Recursively traverse the right subtree
        self._preorder_helper(node.right, result)

# Test cases for the solution
def test_preorder_traversal():
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
    assert solution.preorderTraversal(root) == [1, 2, 3], "Test case 1 failed!"

    # Test case 2: Empty tree
    root = None
    
    assert solution.preorderTraversal(root) == [], "Test case 2 failed!"

    # Test case 3: Tree [1]
    # Tree structure:
    #    1
    root = TreeNode(1)
    
    assert solution.preorderTraversal(root) == [1], "Test case 3 failed!"

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
    
    assert solution.preorderTraversal(root) == [2, 3, 5, 7, 4, 6], "Test case 4 failed!"

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
    
    assert solution.preorderTraversal(root) == [1, 2, 3, 4, 5], "Test case 5 failed!"

    # Test case 6: Tree with only right children [1, None, 2, None, 3, None, 4, None, 5]
    # Tree structure:
    #    1
    #     \
    #      2
    #       \
    #        3
    #         \
    #          4
    #           \
    #            5
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.right.right.right.right = TreeNode(5)
    
    assert solution.preorderTraversal(root) == [1, 2, 3, 4, 5], "Test case 6 failed!"

    # Test case 7: Balanced tree [1, 2, 3, 4, 5, 6, 7]
    # Tree structure:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    assert solution.preorderTraversal(root) == [1, 2, 4, 5, 3, 6, 7], "Test case 7 failed!"

    # Test case 8: Large tree
    # Tree structure:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    #  /     / \
    # 8     9  10
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(10)
    
    assert solution.preorderTraversal(root) == [1, 2, 4, 8, 5, 3, 6, 9, 10, 7], "Test case 8 failed!"

    print("All test cases passed!")

# Run the test cases
test_preorder_traversal()
