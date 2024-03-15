import random

def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()

    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    num_guesses = 0

    while True:
        print("Take a guess.")
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid integer.")
            continue

        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {num_guesses} guesses!")
            break

if __name__ == "__main__":
    guess_the_number()
