import unittest
from is_subsequence import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.mergeAlternately("abc", "ahbgdc")
        self.assertEqual(result, True)

    def test_case_2(self):
        sol = Solution()
        result = sol.mergeAlternately("axc", "ahbgdc")
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
