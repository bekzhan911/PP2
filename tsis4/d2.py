from datetime import date, timedelta

# Get the current date
current_date = date.today()


yesterday = current_date - timedelta(days=1)
today = current_date
tomorrow = current_date - timedelta(days=1)

# Print the results
print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

"""
#Using the datetime module directly:
import datetime

# Get today's date
today = datetime.date.today()

# Calculate yesterday and tomorrow
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

# Print the results
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
"""