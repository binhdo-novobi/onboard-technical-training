from datetime import datetime
from pytz import timezone


# Exercise 1:
# Get the current date, datetime and print out to the screen.
def exercise_1():
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    print(current_date)
    print(current_datetime)


# Exercise 2:
# Get the current datetime of the timezone `GMT +7` and convert it into `UTC`, `GMT` and print out to the screen.
def exercise_2():
    current_datetime = datetime.now(timezone("Etc/GMT-7"))  # It's GMT+7
    current_datetime_utc = current_datetime.astimezone(timezone("UTC"))
    current_datetime_gmt = current_datetime.astimezone(timezone("Etc/GMT"))
    print(current_datetime)
    print(current_datetime_utc)
    print(current_datetime_gmt)


# Exercise 3:
# Convert the following date string into date and print out as following format `dd/mm/yyyy`
# yyyy-mm-dd
# 2021-07-04
def exercise_3(str_date):
    date = datetime.strptime(str_date, "%Y-%m-%d")
    print(date.strftime("%d/%m/%Y"))


if __name__ == "__main__":
    print("Exercise 1:")
    exercise_1()

    print("\nExercise 2:")
    exercise_2()

    print("\nExercise 3:")
    str_date = "2021-07-04"
    exercise_3(str_date)

