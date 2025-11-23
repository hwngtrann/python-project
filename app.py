print("Welcome! This is my Productivity Calculator.")

task_count = input("How many tasks did you complete today? ")
# Convert to number
task_count = float(task_count)

# Estimate weekly productivity
weekly_tasks = task_count * 7
print(f"If you keep this pace, you will complete about {weekly_tasks} tasks this week!")
