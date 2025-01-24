<<<<<<< HEAD
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static Method: Performs addition
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method: Performs multiplication and prints calculation type
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# main.py
=======
# Calculator class with static and class methods
class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute
    
    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Class method that uses a class attribute and multiplies two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
# main.py 
>>>>>>> 8a20141e46704b7df1e8dd178902557ef0d9d434
from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
