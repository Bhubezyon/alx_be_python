def safe_devide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        result = numerator / denominator
        return f"The result of t5he division is: {result:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    
    