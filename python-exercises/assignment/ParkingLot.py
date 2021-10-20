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

class ParkingLot():
    """
    Parking Lot object
    @params:
        capacity: size of the parking lot
    """
    def __init__(self, capacity):
        self.car_count = 0
        self.slots = dict.fromkeys([i for i in range(1, int(capacity)+1)])
        self.table = PrettyTable()