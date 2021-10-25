import re

def exercise_1(inp):

    # Check for occurence of AM or PM at the end of the string.
    check = re.search("[AP]M$", inp)
    if check:

        # Get the starting position of the occurence
        pos = int(check.span()[0])

        # Adding a space at that position
        result = inp[:pos] + ' ' + inp[pos:]
        print(result)

    else:
        print("Please input the correct format.")

if __name__ == "__main__":

    inp = "10:59AM"
    exercise_1(inp)