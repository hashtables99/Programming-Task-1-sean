
# The computer chooses a secret number between 1 and 100.
# You have to try guess the number. After each guess, the game will tell you
# if your guess is too high, too low, or just right.
# The game keeps going until you guess the correct number.
#
# Why this works:
# - The computer picks a random number so every game is different.
# - A loop keeps asking you to guess until you get it right.
# - The game checks your input to make sure it’s a number and gives hints to help you win.

from random import randint # used to create random numbers

def number_guessing_game():

    secret_number = randint(1, 100)  # The computer picks a number between 1 and 100
    
    # keeps checking if the number has been found
    number_found = False
    while number_found == False:  # This loop keeps asking for guesses until you win
        try:  # We use this to catch mistakes, like if you type letters instead of numbers
            guess = int(input("Guess a number between 1 and 100: "))  # Get your guess
            if guess == secret_number:  # If your guess matches the secret number
                print("Correct! You win!")  # Tell you that you won
                break  # Stop the game because you got it right
            elif guess < secret_number:  # If your guess is too small
                print("Too low, try again!")  # Tell you to guess a bigger number
            elif guess > secret_number:  # If your guess is too big
                print("Too high, try again!")  # Tell you to guess a smaller number
        except ValueError:  # This runs if you don’t enter a number
            print("Please enter a number!")  # Ask you to try again with a number

# This line starts the game
number_guessing_game()

# Here’s an example of how the game might look when you play:
#
# Guess a number between 1 and 100: 50
# Too high, try again!
# Guess a number between 1 and 100: 25
# Too low, try again!
# Guess a number between 1 and 100: 37
# Correct! You win!
