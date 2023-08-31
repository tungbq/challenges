import unittest
import sys
sys.path.append("..")
from find_the_difference_of_two_arrays import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.findDifference([1,2,3], [2,4,6])
        self.assertEqual(result, [[1,3],[4,6]])

    def test_case_2(self):
        sol = Solution()
        result = sol.findDifference([1,2,3,3], [1,1,2,2])
        self.assertEqual(result, [[3],[]])

if __name__ == '__main__':
    unittest.main()
