def unique_elements(input_list):
    """
    Returns a new list containing unique elements from the input list.

    Args:
        input_list (list): The input list.

    Returns:
        list: A new list with unique elements.
    """
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = unique_elements(input_list)
print(f"Unique elements in the list: {result}")
