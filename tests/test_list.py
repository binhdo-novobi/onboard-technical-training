import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sources')))
import io
import unittest
from unittest import mock
from my_list import *


class TestList(unittest.TestCase):
    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_exercise_1(self, mock_stdout):
        threshold = 15
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        expected_output = "[1, 1, 2, 3, 5, 8, 13]\n"
        exercise_1(a, threshold)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_exercise_2(self, mock_stdout):
        a = [1, 2, 1, 8, 5, 3, 89, 21, 34, 55, 13]
        expected_output = "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]\n"\
                          "[2, 8, 34]\n"\
                          "[1, 1, 5, 3, 89, 21, 55, 13]\n"
        exercise_2(a)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_exercise_3(self, mock_stdout):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expected_output = "[1, 2, 3, 5, 8, 13]\n"
        exercise_3(a, b)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_exercise_4(self):
        a = [5, 10, 15, 20, 25]
        self.assertEqual(exercise_4(a), [5, 25])
        self.assertEqual(exercise_4(a, 3), [5, 10, 15, 20, 25])

    def test_exercise_5(self):
        a = [1, 1, 2, 3, 5, 5, 3, 10, 1]
        expected_output = [1, 2, 3, 5, 10]
        self.assertEqual(exercise_5_1(a), expected_output)
        self.assertEqual(exercise_5_2(a), expected_output)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestList)
    unittest.TextTestRunner(verbosity=2).run(suite)
