#!/usr/bin/env python3
import unittest

from ParkingLot import ParkingLot, create_parking_lot, park, leave, slot_numbers_for_cars_with_colour, registration_numbers_for_cars_with_colour, slot_number_for_registration_number

class TestCar(unittest.TestCase):
    
    def test_get_registration_number(self):
        
        """Happy case of get registration number of a parked car."""
        
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'H-1234', 'White')
        
        parking_slot = parking_lot.get_parking_slots()

        for parked_car in parking_slot.values():
            if parked_car is not None:
                self.assertEqual(parked_car.get_car_registration_number(), 'H-1234')

    def test_get_registration_number_neg(self):
        """
        Negative case of get registration number of a parked car.
        """
        
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'H-1234', 'White')
        
        parking_slot = parking_lot.get_parking_slots()

        for parked_car in parking_slot.values():
            if parked_car is not None:
                self.assertNotEqual(parked_car.get_car_registration_number(), 'A-1234')

    def test_get_color(self):
        
        """Happy case of get registration number of a parked car."""
        
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'H-1234', 'White')
        
        parking_slot = parking_lot.get_parking_slots()

        for parked_car in parking_slot.values():
            if parked_car is not None:
                self.assertEqual(parked_car.get_car_color(), 'White')

    def test_get_color_neg(self):
        """
        Negative case of get color of a parked car.
        """
        
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'H-1234', 'White')
        
        parking_slot = parking_lot.get_parking_slots()

        for parked_car in parking_slot.values():
            if parked_car is not None:
                self.assertNotEqual(parked_car.get_car_color(), 123)

class TestParkingLot(unittest.TestCase):

    def test_get_parked_car(self):
        """
        Happy case: get the number of parked cars
        """
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9923', 'White' )
        park(parking_lot, 'HR-11-BB-0031', 'Black' )
        park(parking_lot, 'HR-13-DH-7237', 'Red' )
        park(parking_lot, 'HR-15-DH-2731', 'Blue' )
        park(parking_lot, 'HR-11-RH-3231', 'Black' )
        
        num_cars = parking_lot.get_parked_cars()
        self.assertEqual(num_cars, 6)

    def test_get_parked_car_neg(self):
        """
        Neg case: get the number of parked cars when does not park any car
        """
        parking_lot = create_parking_lot(6)
        
        num_cars = parking_lot.get_parked_cars()
        self.assertEqual(num_cars, 0)

    def test_create_parking_lot(self):
        """
        Happy case: check if the number of slot created equal the size of the parking lot
        """
        parking_lot = create_parking_lot(6)
        slot = parking_lot.get_parking_slots()
        self.assertEqual(len(slot), 6)

    def test_create_parking_lot_neg(self):
        """
        Neg case: check if the size of the parking lot is odd
        """
        parking_lot = create_parking_lot(7)
        
        self.assertEqual(parking_lot, "The parking lot's capacity must be a positive integer.")

    def test_park_1(self):
        """
        Happy case: test if the allocated slot number is correct
        """
        parking_lot = create_parking_lot(6)
        res = park(parking_lot, 'HR-11-AA-9123', 'White' )
        self.assertEqual(res, "Allocated slot number: 1")

    def test_park_2(self):
        """
        Happy case: test if the allocated slot number is correct when parking more than 1 cars
        """
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        res = park(parking_lot, 'HR-11-AA-9123', 'White' )
        self.assertEqual(res, "Allocated slot number: 2")

    def test_park_3(self):
        """
        Happy case: test if the returned string is correct when parking more cars than the size of the parking lot
        """
        parking_lot = create_parking_lot(2)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9923', 'White' )
        res = park(parking_lot, 'HR-11-BB-0031', 'Black' )
        self.assertEqual(res, "Parking lot is full.")

    def test_leave(self):
        """
        Happy case: normal leave
        """
        parking_lot = create_parking_lot(2)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9999', 'White' )
        res = leave(parking_lot, 1)
        self.assertEqual(res, 'Car have left at slot number 1.')

    def test_leave_1(self):
        """
        Happy case: leave a car at an unparked slot
        """
        parking_lot = create_parking_lot(4)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9999', 'White' )
        res = leave(parking_lot, 3)
        self.assertEqual(res, 'Slot number 3 does not have any parked car.')

    def test_leave_neg(self):
        """
        Neg case: leave a car at a non-existence slot
        """
        parking_lot = create_parking_lot(2)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9999', 'White' )
        res = leave(parking_lot, 3)
        self.assertEqual(res, 'Slot number 3 does not exist.')

    def test_slot_numbers_for_cars_with_colour(self):
        """
        Happy cases
        """
        parking_lot = create_parking_lot(4)
        park(parking_lot, 'HR-11-AA-9123', 'White')
        park(parking_lot, 'HR-11-AA-9999', 'White')
        park(parking_lot, 'HR-11-BB-0031', 'Black')
        
        res = slot_numbers_for_cars_with_colour(parking_lot, 'White').rstrip(', ')
        self.assertEqual(res, 'Registration numbers for cars with this color: HR-11-AA-9123, HR-11-AA-9999')

    def test_slot_numbers_for_cars_with_colour_no_cars(self):
        """
        Neg cases: parking lot does not have any cars
        """
        parking_lot = create_parking_lot(2)
        
        res = slot_numbers_for_cars_with_colour(parking_lot, 'White').rstrip(', ')
        self.assertEqual(res, 'Parking lot does not have any car.')

    def test_slot_numbers_for_cars_with_colour_no_car(self):
        """
        Happy cases: no parked cars with the input color
        """
        parking_lot = create_parking_lot(4)
        park(parking_lot, 'HR-11-AA-9123', 'White')
        park(parking_lot, 'HR-11-AA-9999', 'White')
        park(parking_lot, 'HR-11-BB-0031', 'Black')
        
        res = slot_numbers_for_cars_with_colour(parking_lot, 'Red').rstrip(', ')
        self.assertEqual(res, 'There is no car with this color.')


    def test_registration_numbers_for_cars_with_colour(self):
        """
        Happy case
        """
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9923', 'White' )
        park(parking_lot, 'HR-11-BB-0031', 'Black' )
        park(parking_lot, 'HR-13-DH-7237', 'Red' )
        park(parking_lot, 'HR-15-DH-2731', 'Blue' )
        park(parking_lot, 'HR-11-RH-3231', 'Black' )
        
        res = registration_numbers_for_cars_with_colour(parking_lot, 'White').rstrip(', ')
        self.assertEqual(res, 'Slot numbers for cars with this color: 1, 2')

    def test_registration_numbers_for_cars_with_colour_no_car(self):
        """
        Happy cases: no parked cars with the input color
        """
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9923', 'White' )
        park(parking_lot, 'HR-11-BB-0031', 'Black' )
        park(parking_lot, 'HR-13-DH-7237', 'Red' )
        park(parking_lot, 'HR-15-DH-2731', 'Blue' )
        park(parking_lot, 'HR-11-RH-3231', 'Black' )
        
        res = registration_numbers_for_cars_with_colour(parking_lot, 'Purple').rstrip(', ')
        self.assertEqual(res, 'There is no car with this color.')

    def test_registration_numbers_for_cars_with_colour_neg(self):
        """
        Neg cases: parking lot does not have any cars
        """
        parking_lot = create_parking_lot(2)
        
        res = registration_numbers_for_cars_with_colour(parking_lot, 'White').rstrip(', ')
        self.assertEqual(res, 'Parking lot does not have any car.')

    def test_slot_number_for_registration_number(self):
        """
        Happy case
        """
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9923', 'White' )
        park(parking_lot, 'HR-11-BB-0031', 'Black' )
        park(parking_lot, 'HR-13-DH-7237', 'Red' )
        park(parking_lot, 'HR-15-DH-2731', 'Blue' )
        park(parking_lot, 'HR-11-RH-3231', 'Black' )
        
        res = slot_number_for_registration_number(parking_lot, 'HR-11-RH-3231').rstrip(', ')
        self.assertEqual(res, 'Slot numbers for cars with this registration number: 6')

    def test_slot_number_for_registration_number_no_car(self):
        """
        Happy cases: no parked cars with the input registration number
        """
        parking_lot = create_parking_lot(6)
        park(parking_lot, 'HR-11-AA-9123', 'White' )
        park(parking_lot, 'HR-11-AA-9923', 'White' )
        park(parking_lot, 'HR-11-BB-0031', 'Black' )
        park(parking_lot, 'HR-13-DH-7237', 'Red' )
        park(parking_lot, 'HR-15-DH-2731', 'Blue' )
        park(parking_lot, 'HR-11-RH-3231', 'Black' )
        
        res = slot_number_for_registration_number(parking_lot, 'ABC-1234').rstrip(', ')
        self.assertEqual(res, 'There is no car with this registration number.')

    def test_slot_number_for_registration_number_neg(self):
        """
        Neg cases: parking lot does not have any cars
        """
        parking_lot = create_parking_lot(2)
        
        res = slot_number_for_registration_number(parking_lot, 'HR-11-RH-3231').rstrip(', ')
        self.assertEqual(res, 'Parking lot does not have any car.')

if __name__ == '__main__':
    unittest.main(verbosity=1)