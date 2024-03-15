def print_permutations(input_string):
    """Print all permutations of the input string."""
    from itertools import permutations
    perm_list = list(permutations(input_string))
    for perm in perm_list:
        print("".join(perm))

# Example usage
user_input = input("Enter a string: ")
print_permutations(user_input)
