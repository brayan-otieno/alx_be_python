# File: temp_conversion_tool.py

# Global conversion factors (defined properly at the top)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius using the global conversion factor.
    This function takes in Fahrenheit and returns the temperature in Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # Accessing the global variable
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit using the global conversion factor.
    This function takes in Celsius and returns the temperature in Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # Accessing the global variable
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # User input for temperature to convert
        temperature = float(input("Enter the temperature to convert: "))
        
        # User input for unit of the temperature (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Handling conversion based on user input
        if unit == 'F':
            celsius = convert_to_celsius(temperature)
            return f"{temperature}°F is {celsius}°C"
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            return f"{temperature}°C is {fahrenheit}°F"
        else:
            # Handle invalid unit input
            return "Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit."
    
    except ValueError:
        # Handle the case where the user enters a non-numeric value for temperature
        return "Invalid temperature. Please enter a numeric value."

if __name__ == "__main__":
    result = main()
    print(result)  # Now the result is returned and printed in the main execution flow.
