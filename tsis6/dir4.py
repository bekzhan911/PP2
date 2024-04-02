def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0

# Example usage
user_file_path = input("Enter the path to the text file: ")
line_count = count_lines_in_file(user_file_path)
print(f"Number of lines in '{user_file_path}': {line_count}")
