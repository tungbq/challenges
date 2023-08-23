import unittest
from kids_with_the_greatest_number_of_candies import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.canPlaceFlowers([1,0,0,0,1], 1)
        self.assertEqual(result, True)

    def test_case_2(self):
        sol = Solution()
        result = sol.canPlaceFlowers([1,0,0,0,1], 2)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
