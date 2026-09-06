# Day 22 – Pong Game

## Topics Covered

* Turtle graphics
* The `turtle` module
* Object-Oriented Programming (OOP)
* Creating objects from classes
* Using built-in Turtle objects
* Creating custom classes
* Inheritance
* Class inheritance from `Turtle`
* Using `super()`
* Class methods
* Instance attributes
* Lists
* Lists of objects
* Accessing objects stored in lists
* Coordinates and positioning
* Using `goto()`
* Using `.forward()`
* Using `.setheading()`
* Using `.xcor()` and `.ycor()`
* Using `.distance()`
* Screen setup and configuration
* Keyboard event listeners
* Using `onkey()`
* Using `listen()`
* Passing functions as arguments
* Higher-order functions
* Collision detection
* Detecting collisions with walls
* Detecting collisions with paddles
* Random number generation
* Using `random.choice()`
* Game loops
* `while` loops
* `for` loops
* Conditional statements (`if`, `elif`, `else`)
* Boolean values
* Comparison operators
* Game state management
* Creating reusable game components
* Separating game components into classes
* Building an interactive graphical game
* Building a Pong game from scratch

## Project

### Pong Game

A graphical Pong game built using Python's Turtle graphics library.

The game recreates the classic Pong arcade game using two paddles and a moving ball.

The player controls one paddle using the keyboard, while the opponent controls the other paddle.

The ball continuously moves across the screen and changes direction when it collides with a paddle or the top and bottom walls.

The game demonstrates how multiple objects can interact with each other and how Object-Oriented Programming can be used to organize the different components of a game.

The project uses separate classes for the paddles, ball, and scoreboard.

## How It Works

The program:

1. Creates and configures the Turtle graphics screen.
2. Creates the left and right paddles.
3. Positions the paddles on opposite sides of the screen.
4. Creates the ball.
5. Creates the scoreboard.
6. Sets up keyboard controls for the player's paddle.
7. Starts the game loop.
8. Moves the ball continuously.
9. Detects when the ball reaches the top or bottom wall.
10. Changes the ball's vertical direction when it hits a wall.
11. Detects when the ball reaches a paddle.
12. Changes the ball's horizontal direction when it hits a paddle.
13. Increases the ball's speed as the game progresses.
14. Detects when the ball passes the left or right boundary.
15. Awards a point to the appropriate player.
16. Updates the scoreboard.
17. Resets the ball after a point is scored.
18. Continues the game until the program is stopped.

## Object-Oriented Structure

The Pong game is divided into separate components.

### `Paddle`

The `Paddle` class represents each player's paddle.

The class is built by inheriting from Python's `Turtle` class.

It provides methods for:

- Moving the paddle up
- Moving the paddle down
- Positioning the paddle
- Controlling the paddle using keyboard input

For example:

```python
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
````

Inheritance allows the `Paddle` class to reuse the functionality already provided by the `Turtle` class.

## Ball Movement

The ball moves continuously using its X and Y movement values.

The direction of movement can be controlled by changing the amount added to the ball's coordinates.

For example:

```python
self.x_move = 10
self.y_move = 10
```

The ball's position is then updated repeatedly:

```python
new_x = self.xcor() + self.x_move
new_y = self.ycor() + self.y_move

self.goto(new_x, new_y)
```

When the ball hits the top or bottom wall, the Y movement is reversed:

```python
self.y_move *= -1
```

When the ball hits a paddle, the X movement is reversed:

```python
self.x_move *= -1
```

This creates the bouncing behavior required for the game.

## Collision Detection

The game uses the ball's position and distance from other objects to detect collisions.

For example:

```python
if ball.distance(paddle) < 50:
    ball.bounce_x()
```

The program also checks whether the ball has reached the top or bottom boundaries:

```python
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
```

Collision detection allows the different objects in the game to interact with one another.

## Scoreboard

The scoreboard keeps track of the scores for both players.

When the ball passes one of the paddles, the appropriate player's score is increased.

For example:

```python
score += 1
```

The scoreboard is then updated to display the new score.

This separates score management from the main game logic.

## Code

### Creating a Paddle

```python
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
```

### Moving the Ball

```python
def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move

    self.goto(new_x, new_y)
```

### Bouncing from a Wall

```python
def bounce_y(self):
    self.y_move *= -1
```

### Bouncing from a Paddle

```python
def bounce_x(self):
    self.x_move *= -1
    self.move_speed *= 0.9
```

### Keyboard Controls

```python
screen.listen()

screen.onkey(paddle_a.go_up, "Up")
screen.onkey(paddle_a.go_down, "Down")
```

The functions are passed to `onkey()` without parentheses so that they are executed only when the corresponding key is pressed.

## What I Learned

* How to build a larger graphical program using multiple classes.
* How to create custom classes that inherit from existing Python classes.
* How inheritance allows a class to reuse functionality from another class.
* How to use `super()` when creating a child class.
* How to create a custom `Paddle` class based on the `Turtle` class.
* How to create objects from custom classes.
* How to give objects their own attributes and behavior.
* How to create methods that control the behavior of game objects.
* How to use coordinates to position objects on the screen.
* How to use `.goto()` to move objects to specific positions.
* How to use `.xcor()` and `.ycor()` to retrieve object coordinates.
* How to continuously move an object by repeatedly updating its position.
* How to change an object's direction by modifying movement values.
* How to reverse movement using multiplication by `-1`.
* How to detect collisions between objects.
* How to use `.distance()` for collision detection.
* How to detect when an object reaches a screen boundary.
* How to make the ball bounce from the top and bottom walls.
* How to make the ball bounce from the paddles.
* How to detect when the ball passes a paddle.
* How to reset the ball after a player scores.
* How to increase the ball's speed as the game progresses.
* How to create and control multiple objects at the same time.
* How to use keyboard event listeners.
* How to use `screen.listen()` to enable keyboard input.
* How to use `screen.onkey()` to connect keyboard keys to functions.
* How to pass functions as arguments without immediately calling them.
* How functions can be treated as first-class objects.
* How to manage the state of a game using variables and objects.
* How to create a scoreboard to track player scores.
* How to separate different responsibilities into different classes.
* How to combine OOP, loops, functions, events, coordinates, and collision detection.
* How to build a complete interactive graphical game.
* How to organize a larger Python project into multiple modules.
* How to build on concepts learned from previous Turtle projects.
* How to compare my own implementation with the instructor's solution and understand different approaches to solving the same problem.

## Challenges

* Understanding how inheritance works in Python.
* Understanding how a custom class can inherit from the `Turtle` class.
* Understanding the purpose of `super()`.
* Creating a reusable `Paddle` class.
* Positioning the paddles correctly on opposite sides of the screen.
* Understanding how the ball's X and Y movement values control its direction.
* Making the ball move continuously.
* Making the ball bounce correctly from the top and bottom walls.
* Detecting when the ball is close enough to a paddle to count as a collision.
* Making the ball bounce correctly when it hits a paddle.
* Detecting when the ball passes the left or right side of the screen.
* Resetting the ball after a point is scored.
* Keeping track of the scores for both players.
* Updating the scoreboard when a player scores.
* Connecting keyboard keys to paddle movement.
* Understanding why functions are passed to `onkey()` without parentheses.
* Managing multiple objects and their interactions at the same time.
* Understanding how different classes communicate through objects and methods.
* Coordinating the ball, paddles, and scoreboard within the game loop.
* Debugging problems involving object movement and collision detection.
* Managing the game state while the game is continuously running.
* Understanding how increasing the ball's speed affects gameplay.
* Structuring a larger project into separate modules and classes.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add stronger input handling for the game controls.
* Add a start screen.
* Add a countdown before each round.
* Add a pause and resume feature.
* Add a "Play Again?" option.
* Add a proper game-over condition.
* Add a winning score such as first to 5 or first to 10.
* Add different difficulty levels.
* Allow the player to choose the ball speed.
* Improve the opponent AI.
* Add a computer-controlled opponent with different difficulty levels.
* Add different paddle sizes.
* Add different ball sizes.
* Add different ball speeds.
* Add obstacles to the playing field.
* Add power-ups.
* Add sound effects for paddle and wall collisions.
* Add background music.
* Improve the visual presentation of the game.
* Add animations and visual effects.
* Add player names.
* Track wins and losses across multiple games.
* Add a high-score system.
* Save game statistics to a file.
* Add a pause menu.
* Create a proper graphical user interface.
* Separate the game engine from the user interface even further.
* Add automated tests for the game logic.
* Refactor the project to make the game components more reusable.
* Expand the project into a more complete Pong-style arcade game.
