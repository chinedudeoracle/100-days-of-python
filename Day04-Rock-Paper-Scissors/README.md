# Day 4 – Rock Paper Scissors

## Topics Covered

- Lists
- List indexing
- User input with `input()`
- Converting input to integers with `int()`
- Conditional statements (`if`, `elif`, `else`)
- Comparison operators
- Random number generation with `random.randint()`
- Input validation
- Logical flow and decision-making

## Project

### Rock Paper Scissors

A simple command-line Rock Paper Scissors game where the player chooses Rock, Paper, or Scissors and competes against a randomly generated computer choice.

The program checks the player's input, displays both choices, and determines whether the player wins, loses, or draws.

## How It Works

The player chooses an option by entering a number:

- `0` – Rock
- `1` – Paper
- `2` – Scissors

The program then:

1. Checks whether the player's input is valid.
2. Displays the player's choice.
3. Randomly generates the computer's choice.
4. Displays the computer's choice.
5. Compares both choices to determine the outcome.
6. Displays whether the player wins, loses, or draws.

## Example

```text
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.

Rock

Computer Chose:
Scissors

You win!
```

## What I Learned

- How to store multiple values in a list.
- How list indexing can be used to retrieve an item based on a user's numeric choice.
- How to generate random numbers using `random.randint()`.
- How to validate user input before continuing with the program.
- How to use conditional statements to determine the outcome of a game.
- How to combine multiple conditions using `if` and `elif`.
- How the order of conditional statements can affect program logic.
- How to handle the special cases where Rock beats Scissors and Scissors loses to Rock.
- How to build a simple interactive game using Python.

## Challenges

- Understanding how to represent the three choices using list indexes.
- Making sure invalid numbers are detected before accessing the list.
- Handling the special Rock-versus-Scissors cases correctly.
- Structuring the conditional statements so that every possible combination produces the correct outcome.
- Comparing my own approach with the instructor's solution and understanding that the same problem can be solved in different ways.

## Future Improvements

- Allow the player to enter `rock`, `paper`, or `scissors` instead of numbers.
- Add a score counter for the player and computer.
- Allow the player to play multiple rounds.
- Display the final score when the game ends.
- Add input validation that keeps asking until a valid choice is entered.
- Add a "Play Again?" option.
- Add more visual effects or ASCII art.