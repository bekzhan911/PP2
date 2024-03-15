# Get input from the user
try:
    base1 = float(input("Please enter the first base of the trapezoid: "))
    base2 = float(input("Please enter the second base of the trapezoid: "))
    height = float(input("Please enter the height of the trapezoid: "))
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit()

# Calculate the area of the trapezoid
area = 0.5 * (base1 + base2) * height

print(f"\nArea of the trapezoid: {area:.2f}")
