import unittest
import sys
sys.path.append("..")
from number_of_recent_calls import RecentCounter
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        rc = RecentCounter()
        self.assertEqual(rc.ping(1), 1)
        self.assertEqual(rc.ping(100), 2)
        self.assertEqual(rc.ping(3001), 3)
        self.assertEqual(rc.ping(3002), 3)

if __name__ == '__main__':
    unittest.main()
