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

    def test_case_4(self):
        sol = Solution()
        result = sol.findMaxAverage([0,4,0,3,2], 1)
        self.assertEqual(result, 4)

    def test_case_5(self):
        sol = Solution()
        result = sol.findMaxAverage([-1], 1)
        self.assertEqual(result, -1)

    def test_case_6(self):
        sol = Solution()
        result = sol.findMaxAverage([-6662,5432,-8558,-8935,8731,
                                     -3083,4115,9931,-4006,-3284,
                                     -3024,1714,-2825,-2374,-2750,
                                     -959,6516,9356,8040,-2169,
                                     -9490,-3068,6299,7823,-9767,
                                     5751,-7897,6680,-1293,-3486,
                                     -6785,6337,-9158,-4183,6240,
                                     -2846,-2588,-5458,-9576,-1501,
                                     -908,-5477,7596,-8863,-4088,
                                     7922,8231,-4928,7636,-3994,
                                     -243,-1327,8425,-3468,-4218,
                                     -364,4257,5690,1035,6217,
                                     8880,4127,-6299,-1831,2854,
                                     -4498,-6983,-677,2216,-1938,
                                     3348,4099,3591,9076,942,4571,
                                     -4200,7271,-6920,-1886,662,
                                     7844,3658,-6562,-2106,-296,
                                     -3280,8909,-8352,-9413,3513,1352,-8825], 90)
        self.assertEqual(result, 37.25555555555555)

    def test_case_7(self):
        sol = Solution()
        result = sol.findMaxAverage([0,4,0,3,3], 5)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
