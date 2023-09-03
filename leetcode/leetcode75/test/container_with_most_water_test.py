import unittest
import sys
sys.path.append("..")
from container_with_most_water import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.maxArea([1,8,6,2,5,4,8,3,7])
        self.assertEqual(result, 49)

    def test_case_2(self):
        sol = Solution()
        result = sol.maxArea([1,1])
        self.assertEqual(result, 1)

    def test_case_3(self):
        sol = Solution()
        result = sol.maxArea([0,2])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
