from guessing_game_art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")

def guessing_game():

    while True:
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_level == "easy":
            attempts = 10
            break
        elif difficulty_level == "hard":
            attempts = 5
            break
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

    guess_number = random.randint(1, 100)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > guess_number:
            print("Too high.")
        elif guess < guess_number:
            print("Too low.")
        elif guess == guess_number:
            win_text = "The number you guessed is right! Congratulations! You Win"
            return win_text

        attempts -= 1
        if attempts > 0:
            print("Guess again.")
    lose_text = "Sorry! Game Over! You lose"
    return lose_text

print(guessing_game())




