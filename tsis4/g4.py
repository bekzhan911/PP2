def squares(a, b):
    """
    Generates the square of numbers from a to b (inclusive).
    """
    for num in range(a, b + 1):
        yield num ** 2

# Example usage:
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

print("Squares of numbers from", a, "to", b, "are:")
for square in squares(a, b):
    print(square, end=", ")
