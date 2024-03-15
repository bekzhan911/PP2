from math import tan, pi

# Get input from the user
try:
    n_sides = int(input("Input number of sides: "))
    s_length = float(input("Input the length of a side: "))
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit()

# Calculate the area of the regular polygon
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))

print(f"The area of the polygon is: {p_area:.6f}")
