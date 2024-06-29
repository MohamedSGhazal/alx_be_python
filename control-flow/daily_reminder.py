task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        reminder = f"Reminder: {task} is a high priority task"
    case _:
        reminder = f"Note: {task} is a {priority} priority task"
if time_bound == "yes":
    reminder += f" that requires immediate attention today!"
else:
    reminder += f" Consider completing it when you have free time."
print(f"{reminder}")