import string

def generate_alphabet_files():
    alphabet = string.ascii_uppercase

    for letter in alphabet:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the content of {file_name}\n")
        print(f"File '{file_name}' created successfully.")

# Generate the alphabet files
generate_alphabet_files()
