import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sources')))
import unittest
from my_dictionary import *


class TestDictionary(unittest.TestCase):
    def test_exercise_1(self):
        price_list = {
            "PowerCore": 790000,
            "PowerLine": 200000,
            "PowerPort": 750000
        }
        order_1 = [{"PowerCore": 1}, {"PowerLine": 1}]
        order_2 = [{"PowerLine": 2}]
        order_3 = [{"PowerCore": 1}, {"PowerPort": 2}]
        expected_output = {
            "PowerCore": 1580000,
            "PowerLine": 600000,
            "PowerPort": 1500000
        }
        self.assertEqual(exercise_1(price_list, order_1, order_2, order_3), expected_output)

    def test_exercise_2(self):
        order = [
            {
                "product": "PowerCore",
                "ordered_qty": 2,
                "delivered_qty": 0
            },
            {
                "product": "PowerLine",
                "ordered_qty": 5,
                "delivered_qty": 0
            },
            {
                "product": "PowerPort",
                "ordered_qty": 3,
                "delivered_qty": 0
            }
        ]
        delivery_order = [
            {
                "product": "PowerCore",
                "delivered_qty": 2
            },
            {
                "product": "PowerLine",
                "delivered_qty": 3
            }
        ]
        expected_output = [
            {
                "product": "PowerCore",
                "ordered_qty": 2,
                "delivered_qty": 2
            },
            {
                "product": "PowerLine",
                "ordered_qty": 5,
                "delivered_qty": 3
            },
            {
                "product": "PowerPort",
                "ordered_qty": 3,
                "delivered_qty": 0
            }
        ]
        exercise_2(order, delivery_order)
        self.assertEqual(order, expected_output)

    def test_exercise_3(self):
        order = [
            {
                "product": "PowerCore",
                "ordered_qty": 2,
            },
            {
                "product": "PowerLine",
                "ordered_qty": 5,
            },
            {
                "product": "PowerPort",
                "ordered_qty": 3,
            },
            {
                "product": "PowerCore",
                "ordered_qty": 1,
            },
            {
                "product": "PowerPort",
                "ordered_qty": 1,
            }
        ]
        expected_output = [
            {
                "product": "PowerCore",
                "ordered_qty": 3
            },
            {
                "product": "PowerLine",
                "ordered_qty": 5
            },
            {
                "product": "PowerPort",
                "ordered_qty": 4
            }
        ]
        self.assertEqual(exercise_3(order), expected_output)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDictionary)
    unittest.TextTestRunner(verbosity=2).run(suite)
