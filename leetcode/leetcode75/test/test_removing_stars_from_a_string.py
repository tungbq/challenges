import unittest
import sys
sys.path.append("..")
from removing_stars_from_a_string import Solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        s1 = "leet**cod*e"
        result = sol.removeStars(s1)
        self.assertEqual(result, "lecoe")

    def test_case_2(self):
        sol = Solution()
        s2 = "leet**cod*eaaaa**de*"
        result = sol.removeStars(s2)
        self.assertEqual(result, "lecoeaad")

    def test_case_3(self):
        sol = Solution()
        s3 = ""
        result = sol.removeStars(s3)
        self.assertEqual(result, "")

    def test_case_4(self):
        sol = Solution()
        s4 = "abvc****"
        result = sol.removeStars(s4)
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()