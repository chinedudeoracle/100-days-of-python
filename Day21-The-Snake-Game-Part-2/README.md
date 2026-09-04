# Day 21 – Snake Game Part 2

## Topics Covered

* Turtle graphics
* The `turtle` module
* Object-Oriented Programming (OOP)
* Creating multiple Turtle objects
* Lists
* Lists of objects
* Accessing objects stored in a list
* Classes and objects
* Creating custom classes
* Class attributes and methods
* Inheritance from existing classes
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
* Using `.xcor()` and `.ycor()`
* Using `.distance()`
* Using `.heading()`
* Using `.setheading()`
* Random number generation
* Using `randint()`
* Detecting collisions
* Collision detection with distance calculations
* Detecting collision with food
* Detecting collision with the wall
* Detecting collision with the snake's tail
* Creating and updating a scoreboard
* Tracking game state
* Updating the snake's length
* Increasing the player's score
* Ending the game
* Creating a game-over state
* Using screen dimensions
* Building an interactive graphical game
* Extending an existing program with additional features

## Project

### Snake Game – Part 2

A complete graphical Snake game built using Python's Turtle graphics library.

This project builds on the Snake Game created in Day 20. The first part focused on creating the snake body, moving the snake, and controlling its direction using the keyboard.

Day 21 adds the main gameplay features that turn the basic snake movement into a complete game.

The snake can now:

- Eat food
- Grow longer when food is eaten
- Increase the player's score
- Display the current score
- Detect collisions with the wall
- Detect collisions with its own tail
- End the game when a collision occurs

The project demonstrates how multiple objects, classes, lists, keyboard events, collision detection, and program state can be combined to create a complete interactive game.

## How It Works

The program:

1. Creates a Turtle graphics screen.
2. Creates the snake using multiple Turtle objects.
3. Stores the snake segments in a list.
4. Creates a food object.
5. Creates a scoreboard.
6. Positions the snake at the starting location.
7. Places the food at a random location.
8. Allows the player to control the snake using the keyboard.
9. Moves the snake continuously.
10. Detects when the snake's head reaches the food.
11. Increases the snake's length when food is eaten.
12. Moves the food to a new random location.
13. Increases the player's score.
14. Updates the scoreboard.
15. Detects when the snake's head reaches the edge of the screen.
16. Detects when the snake's head collides with one of its own tail segments.
17. Ends the game when a collision occurs.
18. Displays the final score.
19. Keeps the graphical window open after the game ends.

## Creating the Food

The game uses a separate object to represent the food.

The food is positioned at a random location on the screen.

When the snake's head gets close enough to the food, a collision is detected.

For example:

```python
if snake.head.distance(food) < 15:
    food.refresh()
````

The food is then moved to another random position so that the player can continue playing.

## Growing the Snake

When the snake eats the food, a new segment is added to the snake's body.

The snake therefore becomes longer as the player's score increases.

The snake's body can be extended by creating another Turtle object and adding it to the list of segments.

```python
def extend(self):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()

    self.segments.append(new_segment)
```

This demonstrates how a list can be used to dynamically manage the number of objects that make up the snake.

## Creating the Scoreboard

The game uses a scoreboard to display the player's current score.

The score increases whenever the snake eats food.

For example:

```python
score += 1
scoreboard.update_score(score)
```

The scoreboard is responsible for displaying the current game state to the player.

## Detecting Collision with Food

The snake's head is checked against the food using Turtle's distance functionality.

```python
if snake.head.distance(food) < 15:
    snake.extend()
    food.refresh()
```

When the distance between the snake's head and the food becomes sufficiently small, the program considers the food eaten.

This demonstrates how distance can be used to detect collisions between objects in a graphical program.

## Detecting Collision with the Wall

The game checks whether the snake's head has moved beyond the boundaries of the screen.

For example:

```python
if (
    snake.head.xcor() > 280
    or snake.head.xcor() < -280
    or snake.head.ycor() > 280
    or snake.head.ycor() < -280
):
    game_is_on = False
```

If the snake reaches the wall, the game ends.

This demonstrates how an object's coordinates can be used to determine whether it has entered or left a particular area.

## Detecting Collision with the Tail

The game also checks whether the snake's head has collided with one of its own body segments.

```python
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        game_is_on = False
```

The first segment is the head, so the program checks the remaining segments for collisions.

If the head gets too close to one of the tail segments, the game ends.

## Code

### Detecting Food Collision

```python
if snake.head.distance(food) < 15:
    snake.extend()
    food.refresh()
    scoreboard.increase_score()
```

### Detecting Wall Collision

```python
if (
    snake.head.xcor() > 280
    or snake.head.xcor() < -280
    or snake.head.ycor() > 280
    or snake.head.ycor() < -280
):
    game_is_on = False
```

### Detecting Tail Collision

```python
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        game_is_on = False
```

These features work together to create the main rules of the Snake game.

## What I Learned

* How to extend an existing Python project by adding new features.
* How to create a separate object to represent the food.
* How to create and manage a scoreboard.
* How to use classes to organize different parts of a game.
* How to add new objects to an existing list.
* How to dynamically increase the number of objects making up the snake.
* How to make the snake grow when it eats food.
* How to use `.distance()` to detect collisions between Turtle objects.
* How to detect when the snake's head reaches the food.
* How to reposition the food after it has been eaten.
* How to generate random positions for the food.
* How to use `.xcor()` and `.ycor()` to check an object's position.
* How to detect when an object reaches the boundary of the screen.
* How to detect collisions between the snake's head and its tail.
* How to use list slicing such as `segments[1:]` to exclude the snake's head.
* How to use loops to check multiple objects for collisions.
* How to update the player's score during the game.
* How to update information displayed on the screen.
* How to use Boolean variables to control whether a game is still running.
* How to end a game when a collision occurs.
* How to combine multiple collision-detection conditions.
* How to manage the state of multiple objects during a game.
* How to build on an existing program instead of starting from scratch.
* How to separate responsibilities between the snake, food, and scoreboard.
* How to combine classes, objects, lists, loops, functions, keyboard events, and collision detection.
* How to turn the basic Snake movement from Day 20 into a functional game.
* How to structure a larger graphical program into separate components.
* How to debug interactions between multiple objects and game states.
* How to compare my own implementation with the instructor's solution and understand different approaches to solving the same problem.

## Challenges

* Understanding how to add new features to an existing Snake game.
* Creating the food as a separate object.
* Positioning the food randomly on the screen.
* Detecting when the snake's head reaches the food.
* Understanding how `.distance()` can be used for collision detection.
* Making the snake grow when food is eaten.
* Dynamically adding new Turtle objects to the snake.
* Keeping the snake's movement working correctly after adding new segments.
* Creating and updating the scoreboard.
* Keeping the displayed score synchronized with the actual game score.
* Detecting when the snake reaches the edge of the screen.
* Determining appropriate screen boundaries for collision detection.
* Detecting when the snake collides with its own tail.
* Understanding why the head should be excluded when checking for tail collisions.
* Using list slicing to check only the snake's body segments.
* Managing multiple collision conditions in the main game loop.
* Understanding how the game state changes when a collision occurs.
* Making sure the game stops correctly after a collision.
* Coordinating the snake, food, and scoreboard objects.
* Debugging problems involving object positions and collision distances.
* Understanding how separate classes can work together to create one complete game.
* Extending the Day 20 project without breaking the existing movement and control logic.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add a "Game Over" message to the screen.
* Add a "Play Again?" option.
* Add a high-score system.
* Save the highest score to a file.
* Display the high score during gameplay.
* Increase the snake's movement speed as the score increases.
* Add different types of food with different scores.
* Add bonus food that disappears after a short period.
* Add obstacles to the game.
* Add different levels.
* Add progressively smaller play areas.
* Add sound effects.
* Add background music.
* Add visual effects when food is eaten.
* Add animations when the snake grows.
* Improve the graphical presentation of the scoreboard.
* Add a pause and resume feature.
* Add a start screen.
* Add a countdown before the game begins.
* Add different game modes.
* Add two-player support.
* Allow the player to customize the snake's appearance.
* Add different snake colors.
* Add different food shapes.
* Add power-ups.
* Add a temporary speed boost.
* Add a temporary invincibility power-up.
* Refactor the game into separate `Snake`, `Food`, and `Scoreboard` classes.
* Separate game logic from the graphical user interface.
* Add automated tests for the non-graphical game logic.
* Store player statistics in a file or database.
* Expand the project into a more complete Snake game with multiple levels and gameplay mechanics.
