# match_case_calculator.py
# Prompt user for two numbers
# The user can input two numbers and an operation (add, subtract, multiply, divide).
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")
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
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}. ")
                