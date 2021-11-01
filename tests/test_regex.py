import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sources')))
import unittest
from my_regex import *


class TestRegex(unittest.TestCase):
    def test_exercise_1(self):
        t1 = "10:59AM"
        t2 = "12:30PM"
        expected_output_1 = "10:59 AM"
        expected_output_2 = "12:30 PM"
        self.assertEqual(exercise_1(t1), expected_output_1)
        self.assertEqual(exercise_1(t2), expected_output_2)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRegex)
    unittest.TextTestRunner(verbosity=2).run(suite)
