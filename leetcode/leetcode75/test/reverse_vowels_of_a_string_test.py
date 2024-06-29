import unittest
import sys
sys.path.append("..")
from reverse_vowels_of_a_string import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.reverseVowels("leetcode")
        self.assertEqual(result, "leotcede")

    def test_case_2(self):
        sol = Solution()
        result = sol.reverseVowels("hello")
        self.assertEqual(result, "holle")

    def test_case_2(self):
        sol = Solution()
        result = sol.reverseVowels("aA")
        self.assertEqual(result, "Aa")

if __name__ == '__main__':
    unittest.main()
