import re


# Exercise 1
def exercise_1(t):
    t = re.sub("AM", " AM", t)
    t = re.sub("PM", " PM", t)
    return t


if __name__ == "__main__":
    print("Exercise 1:")
    t1 = "10:59AM"
    t2 = "12:30PM"
    print(exercise_1(t1))
    print(exercise_1(t2))
