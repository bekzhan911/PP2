def multiply_list(my_list):
    result = 1
    for x in my_list:
        result *= x
    return result

list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiply_list(list1))  # Output: 6
print(multiply_list(list2))  # Output: 24
