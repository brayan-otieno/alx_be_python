import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)      # Test simple addition
        self.assertEqual(self.calc.add(-1, 1), 0)     # Test adding negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)      # Test adding zeros
        self.assertEqual(self.calc.add(-5, -10), -15) # Test adding negative numbers
        self.assertEqual(self.calc.add(1000000, 999999), 1999999) # Test large numbers

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Simple subtraction
        self.assertEqual(self.calc.subtract(0, 5), -5) # Subtracting from zero
        self.assertEqual(self.calc.subtract(-1, 1), -2) # Subtracting positive from negative
        self.assertEqual(self.calc.subtract(10, -5), 15) # Subtracting a negative number
        self.assertEqual(self.calc.subtract(1000000, 999999), 1) # Large number subtraction

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)   # Simple multiplication
        self.assertEqual(self.calc.multiply(-1, 5), -5)  # Multiplying negative by positive
        self.assertEqual(self.calc.multiply(0, 10), 0)   # Multiplying by zero
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Multiplying two negative numbers
        self.assertEqual(self.calc.multiply(1000000, 0), 0)  # Multiplying a large number by zero

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)        # Simple division
        self.assertEqual(self.calc.divide(-6, 3), -2)      # Negative dividend
        self.assertEqual(self.calc.divide(7, 2), 3.5)      # Division with float result
        self.assertEqual(self.calc.divide(0, 1), 0)        # Division of zero by any number
        self.assertEqual(self.calc.divide(10, -2), -5)     # Negative divisor

        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))          # Division by zero (positive numerator)
        self.assertIsNone(self.calc.divide(0, 0))          # Division by zero (zero numerator)

if __name__ == '__main__':
    unittest.main()

# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    # Check if the correct number of arguments is provided (3: script name, numerator, denominator)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Get the numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
