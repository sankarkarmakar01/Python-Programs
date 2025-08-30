# Write a program to print the current date and time.

from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Print in a formatted string
print("Current date and time:")
print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))