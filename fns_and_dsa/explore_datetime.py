# from datetime import  datetime, timedelta

def display_current_datetime():
    # Display the current_datetime and time in the format YYYY-MM-DD HH:MM:SS
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

    def calculate_future_date():
        # Prompt the user to enter a number of days and print it in the format YYYY-MM-DD
        number_of_days = int(input("Enter the number of days to add: "))
        future_date = datetime.now() + timedelta(days=number_of_days)
        print(f"Future date after {number_of_days} days: {future_date.strftime('%Y-%m-%d')}")
from datetime import datetime, timedelta
print("Pleaseenter a valid date in the format YYYY-MM-DD")