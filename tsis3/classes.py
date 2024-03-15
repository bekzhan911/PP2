class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        # Get a string from console input
        self.input_string = input("Enter a string: ")

    def printString(self):
        # Print the string in upper case
        print(self.input_string.upper())

# Create an instance of the StringManipulator class
string_manipulator = StringManipulator()

# Get a string from console input
string_manipulator.getString()

# Print the string in upper case
string_manipulator.printString()
