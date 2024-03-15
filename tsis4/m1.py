import math

# Get input from the user
try:
    degree = float(input("Enter an angle in degrees: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Convert degrees to radians
radians = math.radians(degree)

print(f"{degree} degrees is equal to {radians:.6f} radians")
