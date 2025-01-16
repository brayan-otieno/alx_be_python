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

# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
