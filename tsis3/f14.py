def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    """Filter prime numbers from the list."""
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

# Example usage
numbers_list = [2, 3, 5, 7, 10, 11, 13, 17, 20, 23]
prime_numbers = filter_prime(numbers_list)
print(f"Prime numbers in the list: {prime_numbers}")
