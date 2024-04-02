import os

def check_path_access(path):
    try:
        # Check existence
        if os.path.exists(path):
            print(f"Path '{path}' exists.")
        else:
            print(f"Path '{path}' does not exist.")
            return

        # Check readability
        if os.access(path, os.R_OK):
            print(f"Path '{path}' is readable.")
        else:
            print(f"Path '{path}' is not readable.")

        # Check writability
        if os.access(path, os.W_OK):
            print(f"Path '{path}' is writable.")
        else:
            print(f"Path '{path}' is not writable.")

        # Check executability
        if os.access(path, os.X_OK):
            print(f"Path '{path}' is executable.")
        else:
            print(f"Path '{path}' is not executable.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
user_path = input("Enter a path: ")
check_path_access(user_path)
