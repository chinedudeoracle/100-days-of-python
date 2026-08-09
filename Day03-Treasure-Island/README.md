# Day 3 – Treasure Island

## Topics Covered

- Conditional statements (`if`, `elif`, `else`)
- Nested `if` statements
- User input with `input()`
- String methods (`.lower()`, `.strip()`)
- Comparison operators
- Logical flow and decision-making
- Multi-level branching

## Project

### Treasure Island

A text-based adventure game where the player makes a series of choices to find hidden treasure.

The game presents different scenarios based on the player's decisions. Choosing the wrong path leads to a game-over message, while making the correct choices leads to the treasure.

## How It Works

The player makes three main decisions:

1. Choose whether to go **left** or **right** at a crossroads.
2. If they choose left, decide whether to **wait for a boat** or **swim** across the lake.
3. If they wait for the boat, choose between **three doors**: yellow, red, or blue.

Only one sequence of choices leads to the treasure.

## Example

```text
Welcome to Treasure Island.
Your mission is to find the treasure.

You're at a cross road. Where do you want to go?
Type "left" or "right"

left

You've come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for a boat. Type "swim" to swim across.

wait

You arrive at the island unharmed. There is a house with 3 doors.
One red, one yellow and one blue. Which colour do you choose?

yellow

You found the treasure! You Win!
```

## What I Learned

- How to use `if`, `elif`, and `else` to control program flow.
- How to use nested conditional statements to handle multiple levels of decisions.
- How user input can determine which part of a program is executed.
- How `.lower()` can make user input case-insensitive.
- How `.strip()` can remove unwanted spaces around user input.
- How to handle unexpected input using `else`.
- How to build a simple interactive program using conditional logic.

## Challenges

- Understanding how nested `if` statements affect the flow of the program.
- Keeping track of multiple levels of decisions and their possible outcomes.
- Making sure each possible user choice produces the correct result.
- Handling unexpected or invalid user input.
- Structuring the conditional logic so that each decision leads to the appropriate next stage of the game.

## Future Improvements

- Add more paths and possible endings.
- Add additional challenges or puzzles before the player reaches the treasure.
- Add a scoring system.
- Improve input validation so the player is asked again when an invalid choice is entered.
- Add more ASCII art and visual effects.
- Allow the player to restart the game without having to run the program again.