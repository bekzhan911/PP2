from datetime import datetime

# Specify your two datetime objects
date1 = datetime(2024, 3, 9, 12, 50, 0)  # Example: January 1, 2015, 01:00:00
date2 = datetime.now()  # Current date and time

# Calculate the timedelta (difference)
time_difference = date2 - date1

# Get the total duration in seconds
seconds_difference = time_difference.total_seconds()

print(f"{int(seconds_difference)} seconds")
