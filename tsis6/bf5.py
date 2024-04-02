def all_true(my_tuple):
    return all(my_tuple)

# Example usage
tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = (False, False, False)

print(all_true(tuple1))  # Output: True
print(all_true(tuple2))  # Output: False
print(all_true(tuple3))  # Output: False
