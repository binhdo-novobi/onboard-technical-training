#!/usr/bin/env python3

import sys
from prettytable import PrettyTable

class Car:
    """
    Car object
    @params:
        registration_num: Registration number of a car
        color: Color of a car
    """

    def __init__(self, registration_num, color):

        self.registration_num = registration_num
        self.color = color
        self.slot = None

    def get_car_slot(self):

        return self.slot

    def set_car_slot(self, slot):

        self.slot = slot

    def get_car_color(self):
        
        return self.color

    def get_car_registration_number(self):

        return self.registration_num

class ParkingLot:
    """
    Parking Lot object
    @params:
        capacity: size of the parking lot
    """
    def __init__(self, capacity):
        self.car_count = 0 # number of parked cars in the parking lot
        self.parking_slots = dict.fromkeys([i for i in range(1, int(capacity)+1)])

    def get_parked_cars(self):
        return self.car_count

    def get_parking_slots(self):
        return self.parking_slots

    def set_parking_slots(self, slot, car_obj):
        self.parking_slots[slot] = car_obj

def create_parking_lot(capacity):
    """
    Create a parking lot with the given capacity
    """
    result = ''
    if int(capacity) % 2 != 0 or int(capacity) <= 0:
        result = "The parking lot's capacity must be a positive integer."
        return result

    parking_lot = ParkingLot(int(capacity))

    # Comment the following line when running unit tests for easier test verbose.
    print(f"Successfully created a parking lot with {str(capacity)} slots.")
    
    return parking_lot


def park(parking_lot, registration_num, color):
    """
    park the car in the parking lot 
    and prints the allocated slot in the parking lot
    """
    if parking_lot:

        # Check if there are any available slots.
        if not len(parking_lot.get_parking_slots()) <= parking_lot.get_parked_cars():

            parking_slot = parking_lot.get_parking_slots()
            for slot in parking_slot.keys():

                if parking_slot[slot] is None:
                    car = Car(registration_num, color)
                    parking_lot.set_parking_slots(slot, car)
                    car.set_car_slot(slot)
                    parking_lot.car_count += 1
                    result = 'Allocated slot number: ' + str(slot)
                    break

        elif parking_lot.car_count == len(parking_lot.parking_slots):
            result = 'Parking lot is full.'
    else:
        result = 'Parking lot not found.'

    return result
            
def leave(parking_lot, slot_number):
    """
    leave the parking lot from desired slot and prints the leaving slot, 
    given slot number
    """
    if parking_lot:

        if  parking_lot.get_parked_cars() == 0:
            result = 'Parking lot does not have any car.'

        elif int(slot_number) >= 1 and int(slot_number) <= len(parking_lot.get_parking_slots()):
            
            # Get the available parking slots
            parking_slot = parking_lot.get_parking_slots()
            # Get the car object at the given slot number
            value = parking_slot.get(int(slot_number), None)

            if value is not None:

                # Set the parking slot to None and decrease the car count
                parking_lot.set_parking_slots(int(slot_number), None)
                parking_lot.car_count -= 1
                result = 'Car have left at slot number ' + str(slot_number) + '.'
            else:
                result = 'Slot number ' + str(slot_number) + ' does not have any parked car.'
                
        else:
            result = 'Slot number ' + str(slot_number) + ' does not exist.'
    else:
        result = 'Parking lot not found.'

    return result

def status(parking_lot):

    if parking_lot:

        # Get the parking slot dict
        parking_slot = parking_lot.get_parking_slots()

        table = PrettyTable()
        table.clear()
        table.field_names = ['Slot No.', 'Reg No.', 'Color']

        for parked_car in parking_slot.values():
            if parked_car is not None:
                table.add_rows([[str(parked_car.get_car_slot()), str(parked_car.get_car_registration_number()), str(parked_car.get_car_color())]])
        result = 'OK'
    else:
        result = 'Parking lot not found.'
    print(table)
    return result

def slot_numbers_for_cars_with_colour(parking_lot, colour):
    """
    prints the registration number of the cars for the given colour
    """
    result = ''
    if parking_lot:

        if  parking_lot.get_parked_cars() == 0:
            result = 'Parking lot does not have any car.'

        else:
            found_flag = False
            parking_slot = parking_lot.get_parking_slots()

            for parked_car in parking_slot.values():
                if parked_car is not None:
                    if parked_car.get_car_color() == colour:
                        found_flag = True
                        result += str(parked_car.get_car_registration_number()) + ', '           
            result = 'Registration numbers for cars with this color: ' + result
            if not found_flag:
                result = 'There is no car with this color.'
    else:
        result = 'Parking lot not found.'

    return result

def registration_numbers_for_cars_with_colour(parking_lot, colour):
    """
    prints the slot number of the cars for the given colour
    """
    result = ''
    if parking_lot:

        if  parking_lot.get_parked_cars() == 0:
            result = 'Parking lot does not have any car.'

        else:
            found_flag = False
            parking_slot = parking_lot.get_parking_slots()

            for parked_car in parking_slot.values():

                if parked_car is not None:
                    if parked_car.get_car_color() == colour:
                        found_flag = True
                        
                        result += str(parked_car.get_car_slot()) + ', '
            result = 'Slot numbers for cars with this color: ' + result
            if not found_flag:
                result = 'There is no car with this color.'

    else:
        result = 'Parking lot not found.'

    return result

def slot_number_for_registration_number(parking_lot, registration_num):
    result = ''
    if parking_lot:

        if  parking_lot.get_parked_cars() == 0:
            result = 'Parking lot does not have any car.'

        else:
            found_flag = False
            parking_slot = parking_lot.get_parking_slots()

            for parked_car in parking_slot.values():
                if parked_car is not None:
                    if parked_car.get_car_registration_number() == registration_num:
                        found_flag = True
                        # result = 'Slot numbers for cars with this registration number: '
                        result += str(parked_car.get_car_slot()) + ', '
            result = 'Slot numbers for cars with this registration number: ' + result
            if not found_flag:
                result = 'There is no car with this registration number.'
    else:
        result = 'Parking lot not found.'

    return result

def execute(parking_lot, command):
    """
    This function is to execute the command from input file or interactive mode
    """
    if command[0] == 'create_parking_lot':
        parking_lot = create_parking_lot(command[1])
    elif command[0] == 'park':
        print(park(parking_lot, command[1], command[2]))
    elif command[0] == 'leave':
        print(leave(parking_lot, command[1]))
    elif command[0] == 'status':
        status(parking_lot)
    elif command[0] == 'slot_numbers_for_cars_with_colour':
        print(slot_numbers_for_cars_with_colour(parking_lot, command[1]).rstrip(', ')) # rstrip to remove the trailing ,
    elif command[0] == 'slot_number_for_registration_number':
        print(slot_number_for_registration_number(parking_lot, command[1]).rstrip(', ')) # rstrip to remove the trailing ,
    elif command[0] == 'registration_numbers_for_cars_with_colour':
        print(registration_numbers_for_cars_with_colour(parking_lot, command[1]).rstrip(', ')) # rstrip to remove the trailing ,
    else:
        print('Command not found, please try again !!!')

    return parking_lot


def interactive_mode(parking_lot):
    
    try:
        command = input().split()
        while command[0] != 'exit':
            parking_lot = execute(parking_lot, command)
            command = input().split()
    except Exception as e:
        print(e)

def input_file_mode(parking_lot, filename):
    
    try:
        with open(filename) as file:
            commands = file.readlines()
            for command in commands:
                parking_lot = execute(parking_lot, command.replace('\n', '').split())
    except Exception as e:
        print(e)

def main():
    """
    Main driven code
    """
    parking_lot = None
    if len(sys.argv) > 1:
        input_file_mode(parking_lot, sys.argv[1])
    else:
        interactive_mode(parking_lot)

if __name__ == '__main__':
    main()