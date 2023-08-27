import unittest
import sys
sys.path.append("..")
from move_zeroes import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.moveZeroes([0,1,0,3,12])
        self.assertEqual(result, [1,3,12,0,0])

    def test_case_2(self):
        sol = Solution()
        result = sol.moveZeroes([0])
        self.assertEqual(result, [0])

    def test_case_3(self):
        sol = Solution()
        result = sol.moveZeroes([1,0,2,0,0,3,12])
        self.assertEqual(result, [1,2,3,12,0,0,0])

    def test_case_4(self):
        sol = Solution()
        result = sol.moveZeroes([1,2,3,4,0,8,0,3,0,2,1,0,0,1])
        self.assertEqual(result, [1,2,3,4,8,3,2,1,1,0,0,0,0,0])


if __name__ == '__main__':
    unittest.main()
