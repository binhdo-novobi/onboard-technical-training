import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sources')))
import io
import unittest
from unittest import mock
import time_machine
from my_datetime import *


class TestDateTime(unittest.TestCase):
    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_exercise_1(self, mock_stdout):
        with time_machine.travel("2021-10-19 14:09:38.123456"):
            exercise_1()
            expected_output = "2021-10-19\n2021-10-19 14:09:38.123456\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_exercise_2(self, mock_stdout):
        with time_machine.travel("2021-10-19 05:09:38.123456+07:00"):
            exercise_2()
            expected_output = "2021-10-19 05:09:38.123456+07:00\n"\
                              "2021-10-18 22:09:38.123456+00:00\n"\
                              "2021-10-18 22:09:38.123456+00:00\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_exercise_3(self, mock_stdout):
        str_date = "2021-07-04"
        exercise_3(str_date)
        expected_output = "04/07/2021\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDateTime)
    unittest.TextTestRunner(verbosity=2).run(suite)
