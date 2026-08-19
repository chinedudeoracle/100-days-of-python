# Day 11 – Blackjack

## Topics Covered

- Functions
- Function parameters
- Function arguments
- Returning values with `return`
- Lists
- List methods such as `.append()`, `.remove()`, and `.index()`
- `for` loops
- `while` loops
- Conditional statements (`if`, `elif`, `else`)
- Boolean variables
- Comparison operators
- Logical operators (`and`, `or`)
- Random selection with `random.choice()`
- User input with `input()`
- String formatting with f-strings
- Handling special cases with conditional logic
- Working with game state
- Building reusable functions
- Recursion and restarting a program
- Clearing the terminal with `os.system()`
- ASCII art
- Building a complete interactive command-line game

## Project

### Blackjack

A command-line Blackjack game where the player competes against the computer.

The player and computer are each dealt two cards. The player can choose to draw additional cards or pass. The computer then draws cards until its score reaches at least 17.

The game determines the winner based on standard Blackjack rules, including handling Aces as either `11` or `1` when necessary.

This project is the first major Capstone Project in the course and combines many of the Python concepts learned during the previous days.

## How It Works

The program:

1. Displays the Blackjack logo.
2. Deals two cards to the player and two cards to the computer.
3. Calculates the score of both hands.
4. Checks for Blackjack.
5. Displays the player's cards and the computer's first card.
6. Allows the player to draw additional cards or pass.
7. Converts an Ace from `11` to `1` when the player's score goes over 21.
8. Ends the player's turn if they go over 21 or achieve Blackjack.
9. Allows the computer to draw cards until its score reaches at least 17.
10. Compares the player's score with the computer's score.
11. Determines whether the player wins, loses, or draws.
12. Allows the player to start another game.

### Special Blackjack Rules

The game handles several important Blackjack situations:

- A starting hand of `[11, 10]` is treated as Blackjack.
- Blackjack is represented by a score of `0` in the program.
- An Ace initially has a value of `11`.
- If an Ace causes the score to exceed 21, it is changed to `1`.
- The computer continues drawing while its score is below 17.
- The game ends when the player gets Blackjack, goes over 21, or chooses to pass.

## Code

```python
def deal_card():
    """Returns a random card from deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculate the score of a hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
```
## What I Learned

- How to build a complete program by combining multiple Python concepts.
- How to define separate functions for different parts of a program.
- How to use functions such as `deal_card()`, `calculate_score()`, and `compare()` to organize code.
- How to use `return` to send values back from functions.
- How to use lists to store the player's and computer's cards.
- How to use `.append()` to add new cards to a hand.
- How to use `.remove()` to remove an Ace from a hand.
- How to use conditional statements to handle different Blackjack situations.
- How to use `while` loops to keep the game running until a condition changes.
- How to use Boolean variables such as `is_game_over` to control a game loop.
- How to use `random.choice()` to randomly select cards.
- How to handle an Ace as either `11` or `1`.
- How to detect Blackjack using both the score and the number of cards.
- How to compare two scores and determine the winner.
- How to use logical operators such as `and` and `or` to combine conditions.
- How to use user input to control whether the player draws another card.
- How to separate game logic into reusable functions.
- How to debug errors caused by incorrect function calls.
- How to identify the difference between calling a function and passing the function itself.
- How to prevent an infinite `while` loop by carefully checking loop conditions.
- How to handle special cases such as the computer having Blackjack.
- How to use `os.system()` to clear the terminal between games.
- How to use ASCII art to improve the presentation of a command-line game.
- How to structure a larger Python project compared with the smaller projects from previous days.

## Challenges

- Understanding how to structure a larger program using multiple functions.
- Understanding how the `deal_card()` function can be reused for both the player and computer.
- Handling Aces correctly when the score goes over 21.
- Understanding why an Ace may need to change from `11` to `1`.
- Detecting Blackjack separately from a normal score of 21.
- Understanding why Blackjack is represented by `0` in the program.
- Keeping track of the player's and computer's scores throughout the game.
- Structuring the `while` loops correctly so the game does not continue indefinitely.
- Understanding the difference between `deal_card()` and `deal_card` when passing or calling a function.
- Debugging a `TypeError` caused by accidentally adding a function object to a list instead of the value returned by the function.
- Understanding how logical operators such as `and` and `or` affect loop conditions.
- Making sure the computer stops drawing cards when it reaches 17 or higher.
- Handling the special case where the computer has Blackjack with a score of `0`.
- Making sure the correct result is displayed for wins, losses, draws, and Blackjack.
- Keeping track of multiple game states and knowing when the game should end.
- Comparing my implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

- Add stronger input validation for the player's choices.
- Prevent the player from entering invalid responses when choosing whether to draw another card.
- Add a betting system using virtual chips.
- Add a balance system that tracks the player's winnings and losses.
- Allow the player to choose different betting amounts.
- Add statistics showing the number of wins, losses, and draws.
- Track the player's Blackjack percentage.
- Add different difficulty levels for the computer.
- Improve the handling of multiple Aces in the same hand.
- Add card suits and visual card representations.
- Add more detailed Blackjack rules such as splitting and doubling down.
- Add the ability for the player to surrender.
- Add a graphical user interface.
- Create a more realistic deck system that prevents cards from being randomly reused indefinitely.
- Separate the game logic from the user interface even further.
- Replace recursive game restarts with a loop-based approach.
- Add automated tests for functions such as `calculate_score()` and `compare()`.