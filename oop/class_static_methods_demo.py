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
