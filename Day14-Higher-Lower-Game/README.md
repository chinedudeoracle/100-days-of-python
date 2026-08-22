# Day 14 – Higher Lower Game

## Topics Covered

- Lists
- Dictionaries
- Accessing dictionary values using keys
- Lists of dictionaries
- `len()` function
- Functions
- Function parameters and arguments
- `return` statements
- `while` loops
- `if` and `else` statements
- Boolean variables
- Comparison operators
- Logical thinking and program flow
- Random number generation with `randint()`
- User input with `input()`
- String formatting with f-strings
- String methods such as `.lower()` and `.strip()`
- Tracking game state
- Updating variables during a game
- Working with imported data from another Python file
- Importing custom modules
- Clearing the terminal with `os.system()`
- Building an interactive command-line game

## Project

### Higher Lower Game

A command-line game where the player compares two randomly selected people, brands, or entities and tries to determine which one has more followers.

The program displays two options, A and B, and the player must guess which option has the higher follower count.

If the player guesses correctly, their score increases and the winner of the comparison becomes the next option A. A new option is then selected for option B.

The game continues until the player makes an incorrect guess.

## How It Works

The program:

1. Imports the game logo, VS artwork, and data.
2. Determines the number of entries available in the data.
3. Randomly selects two different entries.
4. Generates descriptions for both options.
5. Displays the two options to the player.
6. Asks the player to choose which option has more followers.
7. Compares the follower counts of the two options.
8. Checks whether the player's answer is correct.
9. Increases the score when the player guesses correctly.
10. Makes the previous winner the new option A.
11. Selects a new random option B.
12. Continues the game with the updated comparison.
13. Ends the game when the player makes an incorrect guess.
14. Displays the player's final score.

The program also ensures that the same entry is not selected for both A and B.

## Code

```python
def generate_message(index):
    return (
        f"Compare A: {data[index]['name']}, "
        f"a {data[index]['description']}, "
        f"from {data[index]['country']}."
    )


def higher_search(score_a, score_b):
    if score_a > score_b:
        return "a"
    else:
        return "b"
```
## What I Learned

* How to use lists and dictionaries to work with structured data.
* How to access values from dictionaries using keys.
* How to work with a list containing multiple dictionaries.
* How to use `len()` to determine the size of a collection.
* How to define functions that perform specific tasks.
* How to use function parameters and arguments to make functions reusable.
* How to use `return` to send values back from a function.
* How to use `randint()` to randomly select items from a collection.
* How to make sure two randomly selected items are not the same.
* How to use `while` loops to keep a game running until a condition changes.
* How to use Boolean variables to control the state of a game.
* How to compare two values and determine which one is larger.
* How to use user input to control the flow of a program.
* How to use `.lower()` and `.strip()` to process user input.
* How to update variables as the game progresses.
* How to keep track of the player's score.
* How to make the previous winner become the next comparison candidate.
* How to separate different parts of a program into reusable functions.
* How to import data and custom components from other Python files.
* How to use f-strings to create dynamic messages.
* How to prevent duplicate selections when randomly choosing entries.
* How to build a complete interactive game by combining multiple Python concepts.

## Challenges

* Understanding how to access information from dictionaries inside a list.
* Understanding how the `data` list is structured and how its dictionaries are accessed.
* Randomly selecting two different entries from the data.
* Making sure option A and option B are never the same.
* Understanding how to compare the follower counts of two different entries.
* Structuring the game so that the previous winner becomes the next option A.
* Selecting a new option B after every correct answer.
* Keeping track of the player's score throughout the game.
* Managing multiple variables that change as the game progresses.
* Understanding how the `while` loop controls the main game.
* Making sure the game ends when the player's answer is incorrect.
* Keeping the displayed information synchronized with the current A and B selections.
* Understanding how functions can simplify and organize a larger program.
* Handling user input and making it case-insensitive.
* Understanding the flow of data between functions and the main game.
* Debugging the program when multiple variables depend on each other.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add stronger input validation for the player's choice.
* Prevent invalid responses such as characters other than `A` or `B`.
* Add more data and categories to the game.
* Add different difficulty levels.
* Add a high-score system.
* Track the player's highest score across multiple games.
* Add a `"Play Again?"` option after the game ends.
* Add lives or a limited number of incorrect guesses.
* Display the correct answer when the player loses.
* Improve the visual presentation of the game.
* Add animations or other terminal effects.
* Add more detailed statistics about the player's performance.
* Create a graphical user interface.
* Separate the game logic from the user interface even further.
* Improve the random selection logic using `random.choice()` instead of randomly selecting dictionary indexes.
* Refactor the program to make the comparison and game-state logic more concise and reusable.
