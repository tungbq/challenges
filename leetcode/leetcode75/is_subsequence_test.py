import unittest
from is_subsequence import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.isSubsequence("abc", "ahbgdc")
        self.assertEqual(result, True)

    def test_case_2(self):
        sol = Solution()
        result = sol.isSubsequence("axc", "ahbgdc")
        self.assertEqual(result, False)

    def test_case_3(self):
        sol = Solution()
        result = sol.isSubsequence("aa", "aa")
        self.assertEqual(result, True)

    def test_case_4(self):
        sol = Solution()
        result = sol.isSubsequence("a", "b")
        self.assertEqual(result, False)

    def test_case_5(self):
        sol = Solution()
        result = sol.isSubsequence("cvbn", "qwryufhhcsffvqfrboiopjehn")
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
