# pattern_drawing.py

def main():
    # Prompt user for the size of the pattern
    size = int(input("Enter the size of the pattern: "))
    
    # Use a while loop to iterate through each row
    row = 0
    while row < size:
        # Use a for loop to print asterisks on the same line
        for col in range(size):
            print("*", end="")  # Print asterisk without moving to a new line
        print()  # Move to the next line after printing a row of asterisks
        row += 1  # Increment the row counter

# Call the main function to execute the script
if __name__ == "__main__":
    main()
