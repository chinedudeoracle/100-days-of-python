# Day 12 – Number Guessing Game

## Topics Covered

* Functions
* Function parameters
* Function arguments
* `return`
* Variables and assignment
* Conditional statements (`if`, `elif`, `else`)
* `while` loops
* Boolean variables
* Comparison operators
* Logical operators (`and`, `or`)
* Random number generation with `random.randint()`
* User input with `input()`
* Converting input with `int()`
* Tracking game state
* Managing attempts/lives
* Difficulty levels
* Function reuse
* Building an interactive command-line game

## Project

### Number Guessing Game

A command-line number guessing game where the player attempts to guess a randomly generated number between 1 and 100.

The player chooses a difficulty level, which determines the number of attempts available. After each guess, the program provides feedback indicating whether the guessed number is too high or too low.

The game continues until the player correctly guesses the number or runs out of attempts.

## How It Works

The program:

1. Displays the game logo and introduction.
2. Generates a random number between 1 and 100.
3. Asks the player to choose a difficulty level.
4. Sets the number of attempts based on the selected difficulty.
5. Asks the player to make a guess.
6. Compares the guess with the secret number.
7. Tells the player whether the guess is too high or too low.
8. Reduces the number of remaining attempts after an incorrect guess.
9. Continues until the player guesses the number or runs out of attempts.
10. Displays a winning message when the player guesses correctly.
11. Displays the correct answer when the player runs out of attempts.

### Difficulty Levels

The game provides two difficulty levels:

* **Easy** – 10 attempts
* **Hard** – 5 attempts

The difficulty level affects how many guesses the player has to find the secret number.

## Code

```python
import random

answer = random.randint(1, 100)

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0
```

## What I Learned

* How to use `random.randint()` to generate a random number within a specified range.
* How to define functions that perform specific tasks.
* How to use function parameters to pass information into a function.
* How to use `return` to send a value back from a function.
* How to use `while` loops to keep the game running while attempts remain.
* How to use `if`, `elif`, and `else` to compare the player's guess with the secret number.
* How to use comparison operators such as `>`, `<`, and `==`.
* How to use Boolean variables to keep track of whether the game is still running.
* How to use user input to make the game interactive.
* How to convert user input from a string to an integer using `int()`.
* How to keep track of the player's remaining attempts.
* How to create different difficulty levels by changing the number of available attempts.
* How to use functions to avoid repeating the same blocks of code.
* How to use a function to check the player's guess and update the number of remaining attempts.
* How to structure a game around a secret value that the player must discover.
* How to provide feedback to the player based on their guess.
* How to combine functions, loops, conditionals, random numbers, and user input to create a complete interactive game.

## Challenges

* Understanding how to generate and store the random target number.
* Understanding how to keep the secret number hidden from the player.
* Keeping track of the number of attempts remaining.
* Understanding how the difficulty level affects the number of available attempts.
* Structuring the `while` loop so the game continues only while attempts remain.
* Making sure an incorrect guess reduces the number of remaining attempts.
* Making sure a correct guess immediately ends the game.
* Understanding how `return` can be used to send the updated number of attempts back to the main program.
* Comparing the player's guess with the secret number and displaying the correct feedback.
* Managing the different possible outcomes of the game.
* Understanding how functions can make the game logic easier to organize and reuse.
* Making sure the program handles the final attempt correctly.
* Comparing my implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add input validation for guesses outside the range of 1–100.
* Prevent the player from entering non-numeric values.
* Add a "Play Again?" option.
* Keep track of the player's score across multiple games.
* Add a leaderboard for high scores.
* Add more difficulty levels.
* Allow the player to choose a custom number range.
* Add hints after a certain number of unsuccessful attempts.
* Add a limited number of special hints that reveal additional information about the secret number.
* Track the number of guesses used to find the answer.
* Add statistics showing the player's average number of guesses.
* Add a graphical user interface.
* Add sound effects and additional ASCII art.
* Create different game modes with different rules and challenges.
