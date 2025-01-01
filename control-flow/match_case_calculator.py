# Prompt the user to input two numbers 
num1 = float(input("Enter the first number:" ))
num2 = float(input("Enter the second number:"))

# Aske the user to choose operation
operation = input("Choose the operation (+, -, *, /): ")
# match_case_calculator.py

def main():
    # Prompt user for input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask for the operation to perform
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation using Match Case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please choose from +, -, *, or /.")

# Call the main function to execute the script
if __name__ == "__main__":
    main()
