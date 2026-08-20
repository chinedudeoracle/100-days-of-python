import random
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def attempts():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        if difficulty == "hard":
            return HARD_LEVEL_TURNS
        elif difficulty == "easy":
            return EASY_LEVEL_TURNS
        else:
            print("Please enter 'easy' or 'hard'.")

def guess_number():
    chosen_number = random.randint(1, 100)
    count = attempts()
    end_guess = False
    while count > 0 and not end_guess:
        print(f"You have {count} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > chosen_number:
            count -= 1
            print(f"Too high.\nGuess again.") 
        elif guess < chosen_number:
            count -= 1
            print(f"Too low.\nGuess again.")
        else:
            end_guess = True
            print(f"You got it! The answer is {guess}")

    if count == 0:
        print("You've run out of guesses, you lose.") 


print(logo)  
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
guess_number()