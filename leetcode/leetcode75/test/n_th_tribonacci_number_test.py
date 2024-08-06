
import unittest
import sys
sys.path.append("..")
from n_th_tribonacci_number import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.tribonacci(0)
        self.assertEqual(result, 0)
    def test_case_2(self):
        sol = Solution()
        result = sol.tribonacci(1)
        self.assertEqual(result, 1)
    def test_case_3(self):
        sol = Solution()
        result = sol.tribonacci(1)
        self.assertEqual(result, 1)
    def test_case_4(self):
        sol = Solution()
        result = sol.tribonacci(4)
        self.assertEqual(result, 4)
    def test_case_5(self):
        sol = Solution()
        result = sol.tribonacci(25)
        self.assertEqual(result, 1389537)
if __name__ == '__main__':
    unittest.main()
