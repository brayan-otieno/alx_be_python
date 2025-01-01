def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    
    # Prompt for the task's priority
    priority = input("Priority (high/medium/low): ").lower()

    # Prompt if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Use Match Case to handle different priorities
    match priority:
        case "high":
            priority_message = "high priority task"
        case "medium":
            priority_message = "medium priority task"
        case "low":
            priority_message = "low priority task"
        case _:
            priority_message = "unknown priority task"

    # Check if the task is time-bound
    if time_bound == "yes":
        time_message = "that requires immediate attention today!"
    else:
        time_message = "Consider completing it when you have free time."

    # Print the customized reminder message
    print(f"Reminder: '{task}' is a {priority_message} {time_message}")

if __name__ == "__main__":
    main()
