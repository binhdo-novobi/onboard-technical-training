from datetime import datetime


# Exercise 1:
def exercise_1():
    year = datetime.today().year
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    line = "Hey {}, in {} you will be 100 years old".format(name, 100 - age + year)
    print(line)
    n = int(input("Enter a number of copies: "))
    [print(line) for _ in range(n)]


# Exercise 2:
def exercise_2():
    name = input("Enter your name: ")
    dob = input("Enter you date of birth (mm/dd/yyyy): ")
    gender = input("Enter your gender: ")
    address = input("Enter your address: ")

    dob = datetime.strptime(dob, "%m/%d/%Y")

    cmd_help = "Available commands: name, age, dob, gender, address, all, help, exit"
    cmd_name = "Your name is {}".format(name)
    cmd_age = "Your age is {}".format(datetime.today().year - dob.year)
    cmd_dob = "Your date of birth is {}".format(dob.date().strftime("%m/%d/%Y"))
    cmd_gender = "Your gender is {}".format(gender)
    cmd_address = "Your address is {}".format(address)

    while True:
        command = input("What would you like to know?\n")
        if command == "exit":
            break
        elif command == "help":
            print(cmd_help)
        elif command == "name":
            print(cmd_name)
        elif command == "age":
            print(cmd_age)
        elif command == "dob":
            print(cmd_dob)
        elif command == "gender":
            print(cmd_gender)
        elif command == "address":
            print(cmd_address)
        elif command == "all":
            print(cmd_name)
            print(cmd_age)
            print(cmd_dob)
            print(cmd_gender)
            print(cmd_address)


if __name__ == "__main__":
    print("Exercise 1:")
    exercise_1()

    print("\nExercise 2:")
    exercise_2()
