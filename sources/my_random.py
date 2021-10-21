import string
import random


# Exercise 1
# Guess number game
def exercise_1():
    answer = random.randint(1, 9)
    turns = 0
    while True:
        try:
            guess = input("Guess number 1-9: ")
            if guess == "exit":
                break
            else:
                guess = int(guess)
            if guess < 1 or guess > 9:
                print("Please guess number in range 1-9")
                continue
            turns += 1
            if guess < answer:
                print("You guess lower.")
            elif guess > answer:
                print("You guess higher.")
            else:
                print("You guess correctly in {} turn(s).".format(turns))
                break
        except ValueError:
            print("Please enter a number!")


# Exercise 2
# Password generator
characters = list(string.ascii_letters + string.digits + "~`!@#$%^&*()_-+={[}]|:;'<,>.?/\"\\")


def exercise_2():
    length = int(input("Enter password length: "))
    random.shuffle(characters)
    password = [random.choice(characters) for _ in range(length)]
    random.shuffle(password)
    password = ''.join(password)
    print(password)


if __name__ == "__main__":
    print("Exercise 1:")
    exercise_1()

    print("\nExercise 2:")
    exercise_2()
