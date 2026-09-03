# Day 20 – Snake Game Part 1

## Topics Covered

* Turtle graphics
* The `turtle` module
* Object-Oriented Programming (OOP)
* Creating multiple Turtle objects
* Lists
* Lists of objects
* Accessing objects stored in a list
* `for` loops
* `while` loops
* Functions
* Function parameters and arguments
* Conditional statements (`if`, `elif`, `else`)
* Boolean values
* Comparison operators
* Keyboard event listeners
* Using `onkey()`
* Using `listen()`
* Passing functions as arguments
* Higher-order functions
* Functions as first-class objects
* Turtle movement
* Coordinates and positioning
* Using `goto()`
* Using `.forward()`
* Using `.left()` and `.right()`
* Using `.heading()`
* Using `.setheading()`
* Controlling multiple objects
* Managing program state
* Building an interactive graphical program
* Building the first part of a Snake game

## Project

### Snake Game – Part 1

A graphical Snake game built using Python's Turtle graphics library.

This is the first part of the Snake Game project. The focus is on creating the snake, moving the snake continuously, and allowing the player to control its direction using the keyboard.

The snake is created from multiple Turtle objects. Each segment is represented by a separate Turtle object, and the segments are stored inside a list.

The snake initially consists of several square segments positioned next to each other.

The project demonstrates how multiple objects can be combined to represent a single game entity and how keyboard events can be used to control an interactive program.

At this stage, the game does **not** include food, scoring, wall collision, or tail collision. Those features will be added in the next part of the project.

## How It Works

The program:

1. Creates a Turtle graphics screen.
2. Creates multiple Turtle objects to represent the snake's body.
3. Gives each segment a square shape.
4. Removes the turtle animation delay where necessary.
5. Positions the snake segments next to each other.
6. Stores the snake segments in a list.
7. Moves the snake continuously.
8. Moves the segments in relation to the segment in front of them.
9. Controls the direction of the snake using keyboard input.
10. Uses event listeners to detect keyboard presses.
11. Prevents the snake from immediately reversing direction.
12. Keeps the game running while the program is active.

## Creating the Snake Body

The snake is created using multiple Turtle objects.

Each segment is represented by a separate Turtle object and stored in a list:

```python
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)
````

The list allows the program to treat the individual Turtle objects as parts of the same snake.

For example:

```python
segments[0]
segments[1]
segments[2]
```

represent individual segments of the snake.

## Moving the Snake

The snake moves by moving each segment toward the position previously occupied by the segment in front of it.

The movement is performed in reverse order so that each segment can follow the segment ahead of it.

For example:

```python
for seg_num in range(len(segments) - 1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(new_x, new_y)

segments[0].forward(MOVE_DISTANCE)
```

The head moves forward first, while the body segments follow the positions of the segments ahead of them.

This creates the appearance of a connected snake moving across the screen.

## Controlling the Snake

Keyboard event listeners are used to control the direction of the snake.

For example:

```python
screen.listen()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
```

The functions are passed to `onkey()` without parentheses.

This means the functions are registered to run when the corresponding keyboard key is pressed.

The direction can be changed using methods such as:

```python
segments[0].setheading(90)
segments[0].setheading(270)
segments[0].setheading(180)
segments[0].setheading(0)
```

## Preventing Immediate Reversal

The snake should not be able to immediately turn back into itself.

For example, when the snake is moving upward, pressing the down key should not be allowed.

This can be handled using conditional statements:

```python
def up():
    if segments[0].heading() != DOWN:
        segments[0].setheading(UP)
```

Similar checks can be used for the other directions.

This introduces the idea of using the current state of an object to determine whether an action should be allowed.

## Keyboard Event Listeners

The program uses the Turtle screen's event-listening functionality.

First, the screen is instructed to listen for keyboard input:

```python
screen.listen()
```

Then functions are associated with specific keys:

```python
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
```

The functions are passed as arguments rather than executed immediately.

This is an example of using functions as first-class objects in Python.

## Code

### Creating the Snake Body

```python
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in STARTING_POSITIONS:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
```

### Moving the Snake

```python
MOVE_DISTANCE = 20

for seg_num in range(len(segments) - 1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(new_x, new_y)

segments[0].forward(MOVE_DISTANCE)
```

### Controlling the Snake

```python
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def up():
    if segments[0].heading() != DOWN:
        segments[0].setheading(UP)


def down():
    if segments[0].heading() != UP:
        segments[0].setheading(DOWN)


def left():
    if segments[0].heading() != RIGHT:
        segments[0].setheading(LEFT)


def right():
    if segments[0].heading() != LEFT:
        segments[0].setheading(RIGHT)
```

The keyboard controls can then be connected to these functions:

```python
screen.listen()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
```

## What I Learned

* How to create multiple Turtle objects.
* How multiple objects can work together to represent one larger object.
* How to store multiple objects inside a list.
* How to access objects stored in a list using indexes.
* How to use a `for` loop to create multiple snake segments.
* How to use coordinates to position the snake segments.
* How to use `.goto()` to move Turtle objects to specific positions.
* How to use `.penup()` to move objects without drawing.
* How to use `.forward()` to move the snake's head.
* How to use `.xcor()` and `.ycor()` to retrieve an object's coordinates.
* How to use `.heading()` to determine the current direction of the snake.
* How to use `.setheading()` to change the direction of the snake.
* How to move objects in reverse order through a list.
* How the snake's body follows the position of the segment in front of it.
* How to use keyboard event listeners.
* How to use `screen.listen()` to enable keyboard input.
* How to use `screen.onkey()` to associate functions with keyboard keys.
* How to pass a function as an argument without immediately calling it.
* How functions can be treated as first-class objects in Python.
* How to use conditional statements to control the snake's direction.
* How to prevent the snake from immediately reversing direction.
* How to use constants to make a program easier to understand and maintain.
* How to organize a graphical program into reusable functions.
* How to manage the state of multiple objects.
* How to combine OOP concepts, lists, loops, functions, and event listeners.
* How to build the foundation of a larger game one feature at a time.

## Challenges

* Understanding how multiple Turtle objects can represent one snake.
* Creating the individual segments of the snake.
* Storing the snake segments in a list.
* Understanding how objects inside a list can be accessed and manipulated.
* Positioning the snake segments correctly at the beginning of the game.
* Understanding how the snake's body follows the head.
* Understanding why the body segments need to be moved in reverse order.
* Using `.xcor()` and `.ycor()` to obtain the position of another segment.
* Understanding how the head and body segments move differently.
* Keeping the distance between snake segments consistent.
* Understanding how the Turtle heading represents direction.
* Using `.setheading()` to change the snake's direction.
* Connecting keyboard keys to functions using `onkey()`.
* Understanding why functions are passed to `onkey()` without parentheses.
* Understanding the difference between passing a function and calling a function.
* Preventing the snake from reversing directly into itself.
* Managing the state of the snake while it is continuously moving.
* Combining keyboard events with continuous movement.
* Understanding how multiple objects can be coordinated to create a single game character.
* Debugging movement and direction-control problems.
* Understanding how the first part of a larger project can provide the foundation for later features.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

The following features will be developed in the next part of the Snake Game:

* Add food for the snake to eat.
* Detect collision between the snake and food.
* Increase the snake's length when food is eaten.
* Create a scoreboard.
* Increase the player's score when food is eaten.
* Detect collision with the wall.
* End the game when the snake hits the wall.
* Detect collision between the snake's head and its tail.
* End the game when the snake collides with its own tail.
* Add a game-over screen.
* Add a high-score system.
* Add a "Play Again?" option.
* Increase the difficulty as the player's score increases.
* Increase the snake's movement speed over time.
* Add different types of food.
* Add obstacles to the game.
* Add sound effects.
* Improve the graphical presentation.
* Add animations.
* Save the player's highest score to a file.
* Create different game modes.
* Refactor the game into separate classes such as `Snake`, `Food`, and `Scoreboard`.
* Add automated tests for the non-graphical game logic.
