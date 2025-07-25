# daily_reminder.py
# Ask the user to input a daily reminder and print it.
# 1. Prompt the user for a reminder.
task = input("Enter your task: ")
# 2. Print the reminder.
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ").strip()
# 3. Provide feedback based on the priority and time-bound status.
match priority:
    case "high":
        print(f"Reminder: {task} - This is a high priority task.")
    case "medium":
        print(f"Reminder: {task} - This is a medium priority task.")
    case "low":
        print(f"Reminder: {task} - This is a low priority task.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
        # 3. Provide feedback based on whether the task is time-bound.
if time_bound == "yes":
    print(f"Reminder: {task} - This task is time-bound. high priority task that requires immediate attention today.")
else:
    print(f"Reminder: {task} - This task is not time-bound. Consider completing it when you have free time.")
    