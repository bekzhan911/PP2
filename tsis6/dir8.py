import os

def delete_file(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Check if the file is writable
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"File '{file_path}' is not writable. Cannot delete.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
user_file_path = input("Enter the path to the file you want to delete: ")
delete_file(user_file_path)
