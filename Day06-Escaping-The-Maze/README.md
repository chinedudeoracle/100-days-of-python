# Day 6 – Escaping the Maze

## Topics Covered

- Custom functions with `def`
- Function calls
- Function composition
- `while` loops
- Conditional statements (`if`, `elif`, `else`)
- Boolean conditions
- Code reuse
- Algorithmic thinking
- Maze navigation

## Project

### Escaping the Maze

A maze-solving program that guides a robot through a maze until it reaches the goal.

The project uses a combination of custom functions, loops, and conditional statements to determine which direction the robot should move.

## How It Works

The program continuously checks the robot's surroundings:

1. If the right side is clear, the robot turns right and moves forward.
2. If the right side is blocked but the front is clear, the robot moves forward.
3. If both the right side and front are blocked, the robot turns left.
4. The process continues until the robot reaches the goal.

The `turn_right()` function is created by combining three `turn_left()` calls.

## Code

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```		
## What I Learned

- How to define a custom function using `def`.
- How functions can be created by combining existing functions.
- How to reuse a function instead of repeating the same code.
- How a `while` loop can keep a program running until a condition changes.
- How `if`, `elif`, and `else` can be used to make decisions.
- How Boolean conditions such as `right_is_clear()` and `front_is_clear()` can control program flow.
- How the order of conditional statements can affect the behavior of a program.
- How to create a simple algorithm for navigating a maze.
- How the same programming concepts can be applied to solve a practical problem.

## Challenges

- Understanding how the `while` loop continues until the robot reaches the goal.
- Understanding how the robot's available paths determine which condition is executed.
- Creating the `turn_right()` function using three `turn_left()` calls.
- Determining the correct order of the `if`, `elif`, and `else` conditions.
- Understanding why the robot should check the right side before checking the front.
- Debugging code that uses functions provided by the Reeborg's World environment rather than standard Python.
- Understanding that VS Code may show warnings for functions such as `move()`, `turn_left()`, and `at_goal()` because they are provided by the external environment.

## Future Improvements

- Create a more general maze-solving algorithm that can handle different maze layouts.
- Explore alternative maze-solving strategies.
- Add comments explaining each step of the algorithm.
- Experiment with different starting positions and maze configurations.
- Investigate how the algorithm behaves when the maze contains loops or dead ends.
- Create a local simulation of the robot so the program can be tested directly in VS Code.
- Explore more advanced pathfinding algorithms such as breadth-first search or A*.