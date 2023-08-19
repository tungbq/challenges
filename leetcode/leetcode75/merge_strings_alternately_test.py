import unittest
from merge_strings_alternately import Solution

class TestSolution(unittest.TestCase):

    def test_merge_equal_lengths(self):
        sol = Solution()
        result = sol.mergeAlternately("abc", "123")
        self.assertEqual(result, "abc123")

    def test_merge_different_lengths_word1_longer(self):
        sol = Solution()
        result = sol.mergeAlternately("abcdef", "12")
        self.assertEqual(result, "a1b2cdef")

    def test_merge_different_lengths_word2_longer(self):
        sol = Solution()
        result = sol.mergeAlternately("xy", "mnopqr")
        self.assertEqual(result, "xmynopqr")

    def test_merge_empty_strings(self):
        sol = Solution()
        result = sol.mergeAlternately("", "")
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()
