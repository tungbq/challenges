import unittest
import sys
sys.path.append("..")
from kids_with_the_greatest_number_of_candies import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.kidsWithCandies([2,3,5,1,3], 3)
        self.assertEqual(result, [True,True,True,False,True])

    def test_case_2(self):
        sol = Solution()
        result = sol.kidsWithCandies([4,2,1,1,2], 1)
        self.assertEqual(result, [True,False,False,False,False])

    def test_case_3(self):
        sol = Solution()
        result = sol.kidsWithCandies([12,1,12], 10)
        self.assertEqual(result, [True,False,True])

if __name__ == '__main__':
    unittest.main()
