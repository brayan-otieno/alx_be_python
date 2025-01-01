# daily_reminder.py

def main():
    # Prompt for task description, priority, and time sensitivity
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Provide a customized reminder based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
        case _:
            reminder = f"Reminder: '{task}' has an invalid priority"

    # Modify reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += " (Invalid time-bound input)"

    # Output the customized reminder
    print(reminder)

# Run the script if it's the main program
if __name__ == "__main__":
    main()
