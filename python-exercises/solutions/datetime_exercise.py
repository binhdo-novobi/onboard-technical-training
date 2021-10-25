from datetime import datetime as dt
import pytz

def exercise_1():

    current_date = dt.today().date()
    current_datetime = dt.now()

    return current_date, current_datetime

def exercise_2(pytz_timezone):

    # Get the current datetime given the GMT + 7 timezone
    current_datetime_gmt7 = dt.now(pytz.timezone(pytz_timezone))
    
    UTC = pytz.timezone("UTC")
    GMT = pytz.timezone("GMT")

    # Convert to UTC and GMT
    current_datetime_utc = current_datetime_gmt7.astimezone(UTC)
    current_datetime_gmt = current_datetime_gmt7.astimezone(GMT)

    return current_datetime_gmt7, current_datetime_utc, current_datetime_gmt
    
    

def exercise_3(date):

    # Parsed the string into datetime object
    parsed_datetime = dt.strptime(date, "%Y-%m-%d")
    
    # Formatted datetime
    formatted_datetime = parsed_datetime.strftime("%d/%m/%Y")

    return formatted_datetime

if __name__ == "__main__":

    # Run exercise 1
    current_date, current_datetime = exercise_1()
    print(f"The current date: {current_date}")
    print(f"The current datetime: {current_datetime}")

    # Run exercise 2
    # "Asia/Ho_Chi_Minh" is a GMT + 7 timezone provided by pytz 
    current_datetime_gmt7, current_datetime_utc, current_datetime_gmt = exercise_2("Asia/Ho_Chi_Minh")
    print(f"GMT + 7: {current_datetime_gmt7}")
    print(f"UTC: {current_datetime_utc}")
    print(f"GMT: {current_datetime_gmt}")

    # Run exercise 3
    formatted_datetime = exercise_3("2021-07-04")
    print(formatted_datetime)