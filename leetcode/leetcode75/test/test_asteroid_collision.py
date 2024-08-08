import unittest
import sys
sys.path.append("..")
from asteroid_collision import Solution
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        asteroids = [5,10,-5]
        expected = [5,10]
        self.assertEqual(sol.asteroidCollision(asteroids), expected)

    def test_case_2(self):
        sol = Solution()
        asteroids = [5,10,11,-20]
        expected = [-20]
        self.assertEqual(sol.asteroidCollision(asteroids), expected)

    def test_case_3(self):
        sol = Solution()
        asteroids = [8, -8]
        expected = []
        self.assertEqual(sol.asteroidCollision(asteroids), expected)

    def test_case_4(self):
        sol = Solution()
        asteroids = [10,2,-5]
        expected = [10]
        self.assertEqual(sol.asteroidCollision(asteroids), expected)

    def test_case_5(self):
        sol = Solution()
        asteroids = [-2,-1,1,2]
        expected = [-2,-1,1,2]
        self.assertEqual(sol.asteroidCollision(asteroids), expected)

    def test_case_6(self):
        sol = Solution()
        asteroids = [10,2,-5,6,7,8,-30,1,2,3]
        expected = [-30,1,2,3]
        self.assertEqual(sol.asteroidCollision(asteroids), expected)

    def test_case_7(self):
        sol = Solution()
        asteroids = [-2,-2,1,-2]
        expected = [-2,-2,-2]
        self.assertEqual(sol.asteroidCollision(asteroids), expected)

if __name__ == '__main__':
    unittest.main()
