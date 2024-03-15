def spy_game(nums):
    # Initialize a variable to keep track of the position of the "0" and "7"
    zero_position = None
    double_zero = False

    # Iterate through the list
    for num in nums:
        if num == 0:
            # If we find a "0", update the position
            zero_position = nums.index(num)
            if double_zero:
                # If we already found one "0", set double_zero to True
                double_zero = False
        elif num == 7 and zero_position is not None:
            # If we find a "7" after a "0", return True
            return True
        elif num == 0 and zero_position is not None:
            # If we find another "0" after the first one, set double_zero to True
            double_zero = True

    # If no "007" sequence is found, return False
    return False

# Example usage
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
