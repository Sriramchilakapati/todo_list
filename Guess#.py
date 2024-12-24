import random
import time

# Function for the introduction
def intro():
    global name
    print("May I ask you for your name?")
    name = input()  # Asking for the player's name
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")

# Function for the guessing logic
def pick():
    number = random.randint(1, 200)  # Generate a random number
    guesses_taken = 0

    while guesses_taken < 6:  # Allow up to 6 guesses
        time.sleep(0.25)
        enter = input("Guess: ")  # Input for the guess

        try:
            # Ensure the input is a number
            guess = int(enter)

            if 1 <= guess <= 200:  # Check if the guess is in range
                guesses_taken += 1  # Increment the guess count

                if guess < number:
                    print("Your guess is too low.")
                elif guess > number:
                    print("Your guess is too high.")
                else:
                    print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
                    return  # Exit the function if guessed correctly

                if guesses_taken < 6:
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")
        except ValueError:
            # Handle non-numeric input
            print(f"I don't think '{enter}' is a number. Please try again.")

    # If all guesses are used up
    print(f"Nope. The number I was thinking of was {number}.")

# Main game loop
play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    intro()
    pick()
    print("Do you want to play again?")
    play_again = input()

print("Thanks for playing!")
