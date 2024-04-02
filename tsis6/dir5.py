def write_list_to_file(file_path, my_list):
    try:
        with open(file_path, 'w') as file:
            for item in my_list:
                file.write(str(item) + '\n')
        print(f"List written to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Example usage
user_file_path = input("Enter the path to the output file: ")
my_list = [1, 2, 3, 4, 5]
write_list_to_file(user_file_path, my_list)
