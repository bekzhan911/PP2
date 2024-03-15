def even_numbers_generator(n):
    """
    Generates even numbers from 0 up to n (inclusive).
    """
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

# Get input from the user
try:
    n = int(input("Enter a positive integer (n): "))
    if n < 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
    exit()

# Generate even numbers and print them in comma-separated form
even_numbers = even_numbers_generator(n)
print("Even numbers from 0 to", n, "are:",  end=" ")
print(*even_numbers, sep=", ")
