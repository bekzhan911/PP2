import os

def analyze_path(path):
    try:
        # Check if the path exists
        if os.path.exists(path):
            print(f"Path '{path}' exists.")
            # Get the filename and directory portion
            filename = os.path.basename(path)
            directory = os.path.dirname(path)
            print(f"Filename: {filename}")
            print(f"Directory: {directory}")
        else:
            print(f"Path '{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
user_path = input("Enter a path: ")
analyze_path(user_path)
