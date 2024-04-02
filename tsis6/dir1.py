import os

def list_directories_files(path):
    try:
        # Remove double quotes if present
        path = path.strip('"')

        # Get a list of all items (directories and files) in the specified path
        all_items = os.listdir(path)

        # Separate directories and files
        directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

        print(f"Directories in {path}:")
        for dir_name in directories:
            print(f"  {dir_name}")

        print(f"\nFiles in {path}:")
        for file_name in files:
            print(f"  {file_name}")

    except FileNotFoundError:
        print(f"Path '{path}' does not exist.")

# Example usage
user_path = input("Enter a path: ")
list_directories_files(user_path)
