def has_33(nums):
    # Iterate through the list (except the last element)
    for i in range(len(nums) - 1):
        # Check if the current and next elements are both 3
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Example usage
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False
