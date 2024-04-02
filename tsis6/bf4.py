from time import sleep
import math

def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)

def main():
    try:
        user_input_number = float(input("Enter a positive number: "))
        user_input_time = float(input("Enter the delay time in milliseconds: "))

        if user_input_number < 0 or user_input_time < 0:
            print("Please enter positive values for both number and time.")
            return

        result = delay(lambda x: math.sqrt(x), user_input_time, user_input_number)
        print(f"Square root of {user_input_number} after {user_input_time} milliseconds is {result:.15f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
