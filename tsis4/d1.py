from datetime import date, timedelta

# Get the current date
current_date = date.today()

# Subtract five days
new_date = current_date - timedelta(days=5)

# Print the results
print(f"Current Date: {current_date}")
print(f"5 days before Current Date: {new_date}")

"""
#if it is asking to Write a Python program to subtract five hour from current time
from datetime import datetime, timedelta

# Get the current time in local timezone
current_time = datetime.now()

# Subtract 5 hours from the current time
new_time = current_time - timedelta(hours=5)

# Convert the new datetime object to a string in a specific format
new_time_str = new_time.strftime('%Y-%m-%d %H:%M:%S')

print(f"Current Time: {current_time}")
print(f"Time 5 hours ago: {new_time_str}")
"""
