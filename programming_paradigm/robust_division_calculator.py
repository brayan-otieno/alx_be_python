# robust_division_calculator.py


def safe_divide(numerator, denominator):
    try:
        # Try to convert both inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        # Catch ValueError if conversion to float fails (non-numeric inputs)
        return "Error: Please enter numeric values only."

    try: 
        # Perform division and return the result
        result = num / denom
    except ZeroDivisionError:
        # Catch ZeroDivisionError if denominator is zero
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result:.2f}"        
