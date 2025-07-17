# match_case_calculator.py
# Prompt user for two numbers
# The user can input two numbers and an operation (add, subtract, multiply, divide).
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    match operation:
        case "add":
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}.")
        case "subtract":
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}.")
        case "multiply":
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}.")
        case "divide":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                print(f"The result of {num1} / {num2} is {result}.")
            print(f"The result of {10} / {0} is (undefined).")
        case _:
            print("Invalid operation: Cannot devide by zero, choose the operation (+, -, *).")