from datetime import datetime, timedelta

# Get the current datetime
current_datetime = datetime.now()

# Remove microseconds
new_datetime = current_datetime.replace(microsecond=0)

# Print the results
print("Current Datetime:", current_datetime)
print("Datetime without Microseconds:", new_datetime)
