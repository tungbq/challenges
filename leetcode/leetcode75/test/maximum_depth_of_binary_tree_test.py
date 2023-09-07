import unittest
import sys
sys.path.append("..")
from maximum_depth_of_binary_tree_test import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.maxDepth([3,9,20,None,None,15,7])
        self.assertEqual(result, 3)

    def test_case_2(self):
        sol = Solution()
        result = sol.maxDepth([1,None,2])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
