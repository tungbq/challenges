import unittest
import sys
sys.path.append("..")
from find_pivot_index import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.pivotIndex([1,7,3,6,5,6])
        self.assertEqual(result, 3)

    def test_case_2(self):
        sol = Solution()
        result = sol.pivotIndex([1,2,3])
        self.assertEqual(result, -1)

    def test_case_3(self):
        sol = Solution()
        result = sol.pivotIndex([2,1,-1])
        self.assertEqual(result, 0)

    def test_case_4(self):
        sol = Solution()
        result = sol.pivotIndex([0])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
