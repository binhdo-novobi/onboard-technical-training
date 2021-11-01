from Car import Car
import argparse


class ParkingLot:
    def __init__(self):
        self.size = 0
        self.slots = []
        self.num_of_occupied_slots = 0

    def create_parking_lot(self, n):
        """
        Create a parking lot
        :param n: number of slots
        :return: False if n is invalid, otherwise True
        """
        if n < 1 or n % 2 != 0:
            return False
        else:
            self.size = n
            self.slots = [-1] * n
            return True

    def get_empty_slot(self):
        """
        Get empty slot
        :return: the first empty slot
        """
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, registration_number, colour):
        """
        A car parks in the parking lot
        :param registration_number: registration number of the car
        :param colour: colour of the car
        :return: the slot number is occupied, -1 if the parking lot is full
        """
        if self.num_of_occupied_slots < self.size:
            empty_slot = self.get_empty_slot()
            self.slots[empty_slot] = Car(registration_number, colour)
            self.num_of_occupied_slots += 1
            return empty_slot + 1
        else:
            return -1

    def leave(self, slot):
        """
        A car leaves the parking lot
        :param slot: the slot number where the car parked
        :return: the slot number, -1 if the slot number is invalid, 0 if there's no car in that slot number
        """
        if slot < 1 or slot > self.size:
            return -1
        elif self.slots[slot - 1] != -1:
            self.slots[slot - 1] = -1
            self.num_of_occupied_slots -= 1
            return slot
        else:
            return 0

    def status(self):
        """
        Print status of the parking lot
        :return:
        """
        print("Slot number   Registration number   Colour          Slot number   Registration number   Colour    ")
        for i in range(0, len(self.slots), 2):
            if self.slots[i] != -1:
                print("{:11d}   {:19s}   {:10s}".format(i + 1, self.slots[i].registration_number, self.slots[i].colour),
                      end="      ")
            else:
                print("{:11d}   {:19s}   {:10s}".format(i + 1, "[empty]", "[empty]"), end="      ")
            if self.slots[i + 1] != -1:
                print("{:11d}   {:19s}   {:10s}".format(i + 2, self.slots[i + 1].registration_number,
                                                        self.slots[i + 1].colour))
            else:
                print("{:11d}   {:19s}   {:10s}".format(i + 2, "[empty]", "[empty]"))

    def slot_numbers_for_cars_with_colour(self, colour):
        """
        Get the slot numbers of cars with specified colour
        :param colour: the colour of the car
        :return: list of slot numbers
        """
        slot_numbers = []
        for i in range(len(self.slots)):
            if self.slots[i] != -1 and self.slots[i].colour == colour:
                slot_numbers.append(str(i + 1))
        return slot_numbers

    def slot_number_for_registration_number(self, registration_number):
        """
        Get the slot number of the car with specified registration number
        :param registration_number: the registration number of the car
        :return: the slot number, -1 if no found
        """
        for i in range(len(self.slots)):
            if self.slots[i] != -1 and self.slots[i].registration_number == registration_number:
                return i + 1
        return -1

    def registration_numbers_for_cars_with_colour(self, colour):
        """
        Get the registration numbers of cars with specified colour
        :param colour: the colour of the car
        :return: list of registration numbers
        """
        registration_numbers = []
        for i in range(len(self.slots)):
            if self.slots[i] != -1 and self.slots[i].colour == colour:
                registration_numbers.append(self.slots[i].registration_number)
        return registration_numbers

    def show(self, line):
        """
        Show the result for each command
        :param line: the command line
        :return:
        """
        args = line.split()
        
        if args[0] == "create_parking_lot":
            n = int(args[1])
            result = self.create_parking_lot(n)
            if result:
                print("Created a parking lot with {} slots.".format(n))
            else:
                print("The size of the parking lot must be a positive and even number.")
        elif args[0] == "park":
            registration_number = args[1]
            colour = args[2]
            result = self.park(registration_number, colour)
            if result != -1:
                print("A car allocated in the slot number {}.".format(result))
            else:
                print("The parking lot is full.")
        elif args[0] == "leave":
            slot = int(args[1])
            result = self.leave(slot)
            if result > 0:
                print("Slot number {} is free.".format(slot))
            elif result < 0:
                print("Invalid slot number.")
            else:
                print("There's no car in slot number {}.".format(slot))
        elif args[0] == "status":
            self.status()
        elif args[0] == "slot_numbers_for_cars_with_colour":
            colour = args[1]
            result = self.slot_numbers_for_cars_with_colour(colour)
            if len(result) == 0:
                print("There's no car with colour {} in the parking lot.".format(colour))
            else:
                print(", ".join(result))
        elif args[0] == "slot_number_for_registration_number":
            registration_number = args[1]
            result = self.slot_number_for_registration_number(registration_number)
            if result != -1:
                print(result)
            else:
                print("There's no car with registration number {} in the parking lot.".format(registration_number))
        elif args[0] == "registration_numbers_for_cars_with_colour":
            colour = args[1]
            result = self.registration_numbers_for_cars_with_colour(colour)
            if len(result) == 0:
                print("There's no car with colour {} in the parking lot.".format(colour))
            else:
                print(", ".join(result))
        elif args[0] == "exit":
            exit(0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='input_file', help="input file")
    args = parser.parse_args()

    # Create ParkingLot object
    parking_lot = ParkingLot()

    # Read command line from file
    if args.input_file:
        with open(args.input_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parking_lot.show(line)
    # Interactive mode
    else:
        while True:
            line = input("$ ")
            parking_lot.show(line)


if __name__ == "__main__":
    main()
