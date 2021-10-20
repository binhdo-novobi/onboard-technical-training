from datetime import datetime as dt

def exercise_1():

    name = input("Please enter your name: ")
    age  = input("Please enter your age: ")
    ans  = f" {name}, you will be 100 years old in the year {int(dt.now().year) + (100 - int(age))}"
    print(ans)
    num  = input("How many times you want to print again: ")

    for i in range(int(num)):
        print(ans)
               
def exercise_2():

    name   = str(input("Please enter your name: "))
    age    = int(input("Please enter your age: "))
    
    dob    = input("Please enter your dob(mm/dd/yyyy): ")
    gender = input("Please enter your gender: ")
    addr   = input("Please enter address: ")

    while True:

        command = input("What would you like to know?\nAvailable commands are: `name`, `age`, `dob`, `gender`, `address`, `all`.\nEnter your command: ")

        if command == "name":
            print(f"Your name is: {name}")

        elif command == "age":
            print(f"Your age is: {age}")

        elif command == "dob":
            print(f"Your date of birth is: {dob}")

        elif command == "gender":
            print(f"Your gender is: {gender}")
            
        elif command == "address":
            print(f"Your address is: {addr}")

        elif command == "all":
            print(f"Your name is: {name}")
            print(f"Your age is: {age}")
            print(f"Your date of birth is: {dob}")
            print(f"Your gender is: {gender}")
            print(f"Your address is: {addr}")
        else:
            command = input('This command is not available. Please enter another: ')
            continue

        break

if __name__ == "__main__":

    # Exercise 1
    # exercise_1()

    # Exercise 2
    exercise_2()