from class_static_methods_demo import Calculator

def main():
    # Using the static method to add two numbers
    sum_result = Calculator.add(5, 10)
    print(f"Sum: {sum_result}")  # Output: Sum: 15

    # Using the class method 
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}") 
    
    if __name__ == "__main__":
        main()