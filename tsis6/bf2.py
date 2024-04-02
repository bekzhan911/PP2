def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    print(f"Number of lowercase characters: {lower_count}")
    print(f"Number of uppercase characters: {upper_count}")

input_string = input("Enter any string: ")
count_upper_lower(input_string)
