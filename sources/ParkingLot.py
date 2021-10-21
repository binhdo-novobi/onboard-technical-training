from Car import Car
import argparse


class ParkingLot:
    def __init__(self):
        self.size = 0
        self.slots = []
        self.num_of_occupied_slots = 0

    def create_parking_lot(self, n):
        if n < 1 or n % 2 != 0:
            return False
        else:
            self.size = n
            self.slots = [-1] * n
            return True

    def get_empty_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, registration_number, colour):
        if self.num_of_occupied_slots < self.size:
            empty_slot = self.get_empty_slot()
            self.slots[empty_slot] = Car(registration_number, colour)
            self.num_of_occupied_slots += 1
            return empty_slot + 1
        else:
            return -1

    def leave(self, slot):
        if slot < 1 or slot > self.size:
            return -1
        elif self.slots[slot - 1] != -1:
            self.slots[slot - 1] = -1
            self.num_of_occupied_slots -= 1
            return slot
        else:
            return 0

    def status(self):
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
        slot_numbers = []
        for i in range(len(self.slots)):
            if self.slots[i] != -1 and self.slots[i].colour == colour:
                slot_numbers.append(str(i + 1))
        return slot_numbers

    def slot_number_for_registration_number(self, registration_number):
        for i in range(len(self.slots)):
            if self.slots[i] != -1 and self.slots[i].registration_number == registration_number:
                return i + 1
        return -1

    def registration_numbers_for_cars_with_colour(self, colour):
        registration_numbers = []
        for i in range(len(self.slots)):
            if self.slots[i] != -1 and self.slots[i].colour == colour:
                registration_numbers.append(self.slots[i].registration_number)
        return registration_numbers

    def show(self, line):
        if line.startswith("create_parking_lot"):
            n = int(line.split()[1])
            result = self.create_parking_lot(n)
            if result:
                print("Created a parking lot with {} slots.".format(n))
            else:
                print("The size of the parking lot must be a positive and even number.")
        elif line.startswith("park"):
            registration_number = line.split()[1]
            colour = line.split()[2]
            result = self.park(registration_number, colour)
            if result != -1:
                print("A car allocated in the slot number {}.".format(result))
            else:
                print("The parking lot is full.")
        elif line.startswith("leave"):
            slot = int(line.split()[1])
            result = self.leave(slot)
            if result > 0:
                print("Slot number {} is free.".format(slot))
            elif result < 0:
                print("Invalid slot number.")
            else:
                print("There's no car in slot number {}.".format(slot))
        elif line.startswith("status"):
            self.status()
        elif line.startswith("slot_numbers_for_cars_with_colour"):
            colour = line.split()[1]
            result = self.slot_numbers_for_cars_with_colour(colour)
            if len(result) == 0:
                print("There's no car with colour {} in the parking lot.".format(colour))
            else:
                print(", ".join(result))
        elif line.startswith("slot_number_for_registration_number"):
            registration_number = line.split()[1]
            result = self.slot_number_for_registration_number(registration_number)
            if result != -1:
                print(result)
            else:
                print("There's no car with registration number {} in the parking lot.".format(registration_number))
        elif line.startswith("registration_numbers_for_cars_with_colour"):
            colour = line.split()[1]
            result = self.registration_numbers_for_cars_with_colour(colour)
            if len(result) == 0:
                print("There's no car with colour {} in the parking lot.".format(colour))
            else:
                print(", ".join(result))
        elif line.startswith("exit"):
            exit(0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='input_file', help="input file")
    args = parser.parse_args()

    parking_lot = ParkingLot()

    if args.input_file:
        with open(args.input_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parking_lot.show(line)
    else:
        while True:
            line = input("$ ")
            parking_lot.show(line)


if __name__ == "__main__":
    main()
