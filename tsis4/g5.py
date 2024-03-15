def countdown_generator(n):
    """
    Generates numbers from n down to 0.
    """
    while n >= 0:
        yield n
        n -= 1

# Example usage:
try:
    n = int(input("Enter a positive integer (n): "))
    if n < 0:
        print("Please enter a positive integer.")
    else:
        print("Countdown from", n, "to 0:")
        for num in countdown_generator(n):
            print(num, end=" ")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
