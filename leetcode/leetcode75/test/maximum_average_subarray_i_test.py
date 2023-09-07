import unittest
import sys
sys.path.append("..")
from maximum_average_subarray_i import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.findMaxAverage([1,12,-5,-6,50,3], 4)
        self.assertEqual(result, 12.75000)

    def test_case_2(self):
        sol = Solution()
        result = sol.findMaxAverage([5], 1)
        self.assertEqual(result, 5.00000)

    def test_case_3(self):
        sol = Solution()
        result = sol.findMaxAverage([1,12,-5,-6,50,3,100,200], 5)
        self.assertEqual(result, 69.4000)

if __name__ == '__main__':
    unittest.main()
