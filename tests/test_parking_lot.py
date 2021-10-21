import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sources')))
import io
import unittest
from unittest import mock
from ParkingLot import ParkingLot


class TestParkingLot(unittest.TestCase):
    def test_create_parking_lot(self):
        parking_lot = ParkingLot()
        result = parking_lot.create_parking_lot(0)
        self.assertFalse(result)
        result = parking_lot.create_parking_lot(1)
        self.assertFalse(result)
        result = parking_lot.create_parking_lot(2)
        self.assertTrue(result)

    def test_park(self):
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        result = parking_lot.park("HR-11-AH-1234", "White")
        self.assertEqual(result, 1)
        result = parking_lot.park("HR-11-AA-9923", "White")
        self.assertEqual(result, 2)
        result = parking_lot.park("HR-11-BB-0031", "Black")
        self.assertEqual(result, -1)

    def test_leave(self):
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        parking_lot.park("HR-11-AH-1234", "White")
        result = parking_lot.leave(0)
        self.assertEqual(result, -1)
        result = parking_lot.leave(3)
        self.assertEqual(result, -1)
        result = parking_lot.leave(2)
        self.assertEqual(result, 0)
        result = parking_lot.leave(1)
        self.assertEqual(result, 1)

    def test_slot_numbers_for_cars_with_colour(self):
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        parking_lot.park("HR-11-AH-1234", "White")
        parking_lot.park("HR-11-AA-9923", "White")
        parking_lot.park("HR-11-BB-0031", "Black")
        result = parking_lot.slot_numbers_for_cars_with_colour("White")
        self.assertEqual(result, ["1", "2"])
        result = parking_lot.slot_numbers_for_cars_with_colour("Red")
        self.assertEqual(result, [])

    def test_slot_number_for_registration_number(self):
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        parking_lot.park("HR-11-AH-1234", "White")
        parking_lot.park("HR-11-AA-9923", "White")
        parking_lot.park("HR-11-BB-0031", "Black")
        result = parking_lot.slot_number_for_registration_number("HR-11-BB-0031")
        self.assertEqual(result, 3)
        result = parking_lot.slot_number_for_registration_number("HR-11-CC-0031")
        self.assertEqual(result, -1)

    def test_registration_numbers_for_cars_with_colour(self):
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        parking_lot.park("HR-11-AH-1234", "White")
        parking_lot.park("HR-11-AA-9923", "White")
        parking_lot.park("HR-11-BB-0031", "Black")
        result = parking_lot.registration_numbers_for_cars_with_colour("White")
        self.assertEqual(result, ["HR-11-AH-1234", "HR-11-AA-9923"])
        result = parking_lot.registration_numbers_for_cars_with_colour("Red")
        self.assertEqual(result, [])

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_status(self, mock_stdout):
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        parking_lot.park("HR-11-AH-1234", "White")
        parking_lot.park("HR-11-AA-9923", "White")
        parking_lot.park("HR-11-BB-0031", "Black")
        parking_lot.status()
        expected_output = \
            "Slot number   Registration number   Colour          Slot number   Registration number   Colour    \n"\
            "          1   HR-11-AH-1234         White                     2   HR-11-AA-9923         White     \n"\
            "          3   HR-11-BB-0031         Black                     4   [empty]               [empty]   \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParkingLot)
    unittest.TextTestRunner(verbosity=2).run(suite)
