# Day 7 – The Hangman

## Topics Covered

- Lists
- List indexing
- `for` loops
- `while` loops
- Conditional statements (`if`, `elif`, `else`)
- Boolean conditions
- User input with `input()`
- String methods such as `.lower()`
- Random selection with `random.choice()`
- String concatenation
- Variables and assignment
- Custom functions
- ASCII art
- Game state and tracking progress
- Input validation
- Building an interactive command-line game

## Project

### The Hangman

A command-line Hangman game where the player attempts to guess a hidden word one letter at a time.

The program randomly selects a word from a predefined word list and gives the player a limited number of lives. Correct guesses reveal letters in the hidden word, while incorrect guesses reduce the player's remaining lives.

The game continues until the player either guesses the word correctly or runs out of lives.

## How It Works

The program:

1. Randomly selects a word from the word list.
2. Creates a display showing blanks for each letter in the word.
3. Asks the player to guess a letter.
4. Checks whether the guessed letter appears in the chosen word.
5. Reveals the correctly guessed letters.
6. Reduces the player's lives when an incorrect letter is guessed.
7. Displays the appropriate Hangman stage based on the number of remaining lives.
8. Continues until the player guesses the word or runs out of lives.
9. Displays a win or game-over message when the game ends.

The project also uses ASCII art to display the Hangman stages and the game logo.

## Code

```python
# Example structure of the Hangman game

import random

chosen_word = random.choice(word_list)

# Game logic continues until the word is guessed
# or the player runs out of lives.
```
## What I Learned

- How to use lists to store collections of words and other values.
- How to randomly select an item from a list using `random.choice()`.
- How to use `for` loops to check each letter in a word.
- How `while` loops can keep a game running until a condition changes.
- How to use `if`, `elif`, and `else` to control the flow of the game.
- How to use Boolean conditions to determine whether a guessed letter is correct.
- How to use user input to make a program interactive.
- How to use `.lower()` to make letter comparisons case-insensitive.
- How to keep track of the player's remaining lives.
- How to update the displayed word as the player makes correct guesses.
- How to use list indexing to access specific items.
- How to use ASCII art to improve the presentation of a command-line program.
- How to organize different stages of a game using a list.
- How to build a complete interactive game by combining several Python concepts.

## Challenges

- Understanding how to compare the player's guessed letter with every letter in the chosen word.
- Keeping track of correctly guessed letters while hiding the remaining letters.
- Making sure a correct guess does not unnecessarily reduce the player's lives.
- Handling incorrect guesses and updating the Hangman stage correctly.
- Understanding how the game should determine when the player has won.
- Understanding how the game should determine when the player has lost.
- Keeping track of the number of remaining lives throughout the game.
- Working with ASCII art and multi-line strings.
- Understanding how external or predefined game components work together with the main program.
- Dealing with VS Code warnings for escape characters used in ASCII art.
- Understanding that functions such as `clear()` may be provided by an external learning environment but are not built-in Python functions.

## Future Improvements

- Allow the player to choose different difficulty levels.
- Add a larger and more varied word list.
- Prevent the same letter from being guessed multiple times.
- Display the letters that have already been guessed.
- Add a score system based on the number of remaining lives.
- Add a "Play Again?" option without restarting the program.
- Add different categories of words.
- Improve the input validation so that only single alphabetic characters are accepted.
- Add additional ASCII art and visual effects.
- Create a local version that can run entirely in VS Code without depending on an external learning environment.