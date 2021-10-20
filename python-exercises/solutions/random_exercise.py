import random 
import string

def exercise_1():
    count = 0
    ans = random.randint(1, 9)
    print("Welcome to the Guessing game. Please guess a number in the range from 0 to 9.")
    print("Or type 'exit' to exit the game.")

    while True:
        
        user_guess = input("Enter your guess: ")
        count += 1

        if user_guess == "exit":
            print("Exit the game.")
            break

        elif user_guess.isdigit():
            if int(user_guess) < ans:
                print("Your guess is too low")

            elif int(user_guess) > ans:
                print("Your guess is too high")
                
            elif int(user_guess) == ans:
                print(f"You have guessed correctly. You took {count} time(s).")
                break
        else:
            print("Unknow input. Please input a number in range [0:9]")

def exercise_2():

    # Get all possible characters
    lowercases = string.ascii_lowercase
    uppercases = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Append all characters into a character pool
    char_pool = lowercases + uppercases + numbers + symbols

    print("Welcome to the password generator.")
    print("Please type in the desired password length.")
    print("Or 'exit' to exit the program.")
    
    password_length = input("Desired password length(in characters): ")

    # Random sample and shuffle the sampled result.
    sampled = random.sample(char_pool, int(password_length))
    l = list(sampled)
    random.shuffle(l)
    result = "".join(l)
    
    # Print the generated password
    print(f"Your password: {result}")

if __name__ == "__main__":

    # Exercise 1
    exercise_1()

    # Exercise 2
    exercise_2()

