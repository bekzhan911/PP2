def divisible_by_3_and_4_generator(n):
    """
    Generates numbers divisible by 3 and 4 from 0 up to n (inclusive).
    """
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

# Example usage:
n = int(input("Enter a positive integer (n): "))
if n < 0:
    print("Please enter a positive integer.")
else:
    print("Numbers divisible by 3 and 4 from 0 to", n, "are:")
    for divisible_num in divisible_by_3_and_4_generator(n):
        print(divisible_num, end=", ")
