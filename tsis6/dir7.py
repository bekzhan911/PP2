def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
            with open(destination_file, 'w') as dest:
                dest.write(content)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")

# Example usage
source_path = input("Enter the path to the source file: ")
destination_path = input("Enter the path to the destination file: ")
copy_file(source_path, destination_path)
