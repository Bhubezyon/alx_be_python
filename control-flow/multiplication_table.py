# multiplication_table.py
# Print a multiplication table for numbers 1 to 10.
# format: "X * Y = Z", where X is the user's input number, Y is the current number in the loop, and Z is the product.
def multiplication_table():
    try:
        number = int(input("Enter a number to generate its multiplication table (1-10): "))
        if number < 1 or number > 10:
            print("Please enter a number between 1 and 10.")
            return
        
        # Loop through numbers 1 to 10 to generate the multiplication table
        print(f"Multiplication table for {number}:")
        for i in range(1, 11):
            result = number * i
            print(f"{number} * {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer between 1 and 10.")
