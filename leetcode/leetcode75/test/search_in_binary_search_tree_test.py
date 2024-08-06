import unittest
import sys
sys.path.append("..")
from search_in_binary_search_tree import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestSolution(unittest.TestCase):
    # TODO: Write a function to print the node
    def test_case_1(self):
        # Test case 1: Trees with same leaf values
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        root_res = TreeNode(2)
        root_res.left = TreeNode(3)

        solution = Solution()
        result = solution.searchBST(root, 2)
        print(result.val)
        print(result.left.val)

if __name__ == '__main__':
    unittest.main()
