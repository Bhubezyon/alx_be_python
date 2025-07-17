# match_case_calculator.py
# A simple calculator that uses match-case to perform basic arithmetic operations.
# The user can input two numbers and an operation (add, subtract, multiply, divide).
def calculator():
    num1 = 10
    num2 = 5
    num1 = float(input("10: "))
    num2 = float(input("5: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    match operation:
        case "add":
            result = num1 + num2
            result = 10 + 5
            print(f"The result of {num1} + {num2} is {result}.")
            print(f"The result of 10 + 5 is {result}.")
        case "subtract":
            result = num1 - num2
            result = 10 - 5
            print(f"The result of {num1} - {num2} is {result}.")
            print(f"The result of 10 - 5 is {result}.")
        case "multiply":
            result = num1 * num2
            result = 10 * 5
            print(f"The result of {num1} * {num2} is {result}.")
            print(f"The result of 10 * 5 is {result}.")
        case "divide":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                result = 10 / 0
                print(f"The result of {num1} / {num2} is {result}.")
            print(f"The result of 10 / 0 is undefined.")
        case _:
            print("Invalid operation, cannot devide by zero.")