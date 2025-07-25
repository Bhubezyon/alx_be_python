# from arithmetic_operations import import perform_operation
def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, devide): ") .strip().lower()

    #result = perform_operation()
    def perform_operation(num1, num2, operation):
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "devide":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation."
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")
    if __name__ == "__main__":
        main()
