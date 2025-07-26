def calculate_future_date():
    from datetime import datetime, timedelta

    # Prompts the user to enter the number of days and calculates the future date
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date and time: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")

    # Get user input for the number of days to add
    days_to_add = int(input("Enter the number of days to add: "))
