def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    
    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")  # Get user's choice

        if choice == '1':
            # Add an item to the list
            item = input("Enter the item to add: ").strip()  # Ask user for the item
            shopping_list.append(item)  # Append the item to the shopping list
            print(f"'{item}' has been added to your shopping list.\n")
        
        elif choice == '2':
            # Remove an item from the list
            item = input("Enter the item to remove: ").strip()  # Ask user for the item
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item if it exists
                print(f"'{item}' has been removed from your shopping list.\n")
            else:
                print(f"'{item}' not found in the shopping list.\n")  # Item not found
            
        elif choice == '3':
            # Display the current shopping list
            if shopping_list:
                print("\nShopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                print()  # Print an empty line for neatness
            else:
                print("\nYour shopping list is empty.\n")
        
        elif choice == '4':
            print("Goodbye!")  # Exit the program
            break
        
        else:
            print("Invalid choice. Please try again.\n")  # Handle invalid menu options

if __name__ == "__main__":
    main()
