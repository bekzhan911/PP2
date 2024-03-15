# Get input from the user
try:
    base_length = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit()

# Calculate the area of the parallelogram
area = base_length * height

print(f"The area of the parallelogram is: {area:.1f}")
