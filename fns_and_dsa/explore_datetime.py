def display_current_datetime():
    from datetime import datetime, timedelta

    # Get the current date and time
    current_datetime = datetime.now()
    print(f"Current date and time: {current_datetime}")

    # Get user input for the number of days to add
    days_to_add = int(input("Enter the number of days to add: "))
    
    # Calculate the future date
    future_datetime = current_datetime + timedelta(days=number_of_days)
    print(f"Future date and time after adding {days_to_add} days: {future_datetime}")
