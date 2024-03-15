# Get the upper limit from the user
try:
    N = int(input("Enter an integer for the upper limit: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Create a list of squares using a list comprehension
squares_list = [(i+1) * (i+1) for i in range(N)]

# Print the list of squares
print("List of squares:")
print(squares_list)
