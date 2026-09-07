# Day 23 – Turtle Crossing

## Topics Covered

* Object-Oriented Programming (OOP)
* Classes
* Objects
* Creating objects from classes
* Inheritance
* Parent and child classes
* Calling methods from inherited classes
* The `turtle` module
* Creating and controlling Turtle objects
* Turtle movement
* Coordinates and positioning
* `goto()`
* `forward()`
* `penup()` and `pendown()`
* Keyboard event listeners
* Using `onkey()`
* Using `listen()`
* Functions
* Function parameters and arguments
* `for` loops
* `while` loops
* Conditional statements (`if`, `elif`, `else`)
* Boolean values
* Comparison operators
* Random number generation with `randint()`
* Random object generation
* Collision detection
* Tracking object positions
* Tracking game state
* Creating multiple objects from the same class
* Managing lists of objects
* Updating objects during a game
* Level progression
* Increasing game difficulty
* Creating a scoreboard
* Using Turtle graphics for interactive games
* Building a complete graphical game

## Project

### Turtle Crossing

A graphical Turtle game inspired by the classic Frogger-style road-crossing concept.

The player controls a turtle and must guide it across a road while avoiding moving cars.

The turtle moves upward when the player presses the appropriate key. Cars are generated at random positions and move horizontally across the screen.

If the turtle successfully reaches the other side of the road, the player advances to the next level.

As the level increases, the cars become faster, making the game progressively more difficult.

The game ends when the turtle collides with a car.

## How It Works

The program:

1. Creates the game screen.
2. Creates the player-controlled turtle.
3. Positions the turtle at the starting point.
4. Allows the player to control the turtle using the keyboard.
5. Creates cars at random positions.
6. Stores the cars in a list.
7. Moves the cars across the screen.
8. Continuously checks whether new cars should be created.
9. Checks whether the turtle has collided with any car.
10. Checks whether the turtle has reached the finish line.
11. Increases the player's level when the turtle successfully crosses the road.
12. Increases the speed of the cars as the level increases.
13. Resets the turtle to the starting position after successfully crossing.
14. Updates the scoreboard.
15. Ends the game when the turtle collides with a car.

## Object-Oriented Structure

The project uses classes to organize the different components of the game.

### `Player`

The `Player` class represents the turtle controlled by the player.

It is responsible for:

- Creating the player turtle.
- Positioning the turtle.
- Moving the turtle upward.
- Detecting when the turtle reaches the finish line.
- Resetting the turtle to the starting position.

### `CarManager`

The `CarManager` class manages the cars in the game.

It is responsible for:

- Creating cars.
- Storing cars in a list.
- Positioning cars randomly.
- Moving cars across the screen.
- Increasing the speed of the cars as the level increases.

### `Scoreboard`

The `Scoreboard` class displays and manages the player's level.

It is responsible for:

- Displaying the current level.
- Updating the level when the player crosses the road.
- Displaying the game-over message.

## Inheritance

The project demonstrates inheritance by creating specialized classes based on the Turtle class.

For example, the `Player` and `CarManager` classes can use functionality provided by the Turtle library while adding their own game-specific behavior.

Inheritance allows a child class to reuse functionality from a parent class instead of implementing everything from scratch.

## Creating and Managing Cars

The game creates multiple cars and stores them in a list.

```python
cars = []

new_car = Turtle("square")
cars.append(new_car)
````

The program can then loop through the list and move every car:

```python
for car in cars:
    car.forward(speed)
```

This allows the game to manage many independent objects using the same class.

## Random Car Generation

Cars are generated at random positions.

Randomness is used to prevent the traffic pattern from being predictable.

For example:

```python
random_y = randint(-250, 250)
```

The program can use the random value to determine where a new car should appear.

## Keyboard Controls

The Turtle screen can listen for keyboard events.

For example:

```python
screen.listen()
screen.onkey(player.move, "Up")
```

When the player presses the specified key, the associated function is executed.

This allows the program to respond to user input in real time.

## Collision Detection

The game continuously checks the distance between the player and the cars.

For example:

```python
if car.distance(player) < 20:
    game_is_on = False
```

If the player gets sufficiently close to a car, the game detects a collision and ends.

## Level Progression

When the player successfully reaches the other side of the road, the level increases.

The game then:

1. Updates the scoreboard.
2. Increases the car speed.
3. Moves the player back to the starting position.
4. Continues the game at the new difficulty level.

This creates progressively more difficult gameplay.

## Code

### Creating the Player

```python
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(10)
```

### Keyboard Control

```python
screen.listen()
screen.onkey(player.move, "Up")
```

### Moving Cars

```python
for car in cars:
    car.forward(car_speed)
```

### Detecting a Collision

```python
if car.distance(player) < 20:
    game_is_on = False
```

### Detecting the Finish Line

```python
if player.ycor() > 280:
    player.reset_position()
    scoreboard.increase_level()
    car_manager.level_up()
```

## What I Learned

* How to create classes for different components of a game.
* How to create objects from custom classes.
* How inheritance allows one class to build on another class.
* How to use `super()` when inheriting from a parent class.
* How to extend the functionality of the `Turtle` class.
* How to create multiple objects from the same class.
* How to store multiple objects in a list.
* How to loop through a list of objects and update them.
* How to create and control Turtle objects.
* How to position objects using coordinates.
* How to use `goto()` to move objects to specific positions.
* How to use `forward()` to move objects.
* How to use `penup()` to move objects without drawing.
* How to use keyboard event listeners.
* How to use `listen()` to allow the screen to receive keyboard input.
* How to use `onkey()` to associate a function with a keyboard key.
* How functions can be used as event handlers.
* How to use `randint()` to generate random values.
* How randomness can be used to create unpredictable game elements.
* How to create multiple cars at random positions.
* How to manage multiple moving objects simultaneously.
* How to detect collisions between game objects.
* How to use the `distance()` method to determine how close two objects are.
* How to track the player's position using Turtle coordinates.
* How to detect when the player reaches a specific position.
* How to create a level system.
* How to increase the difficulty of a game as the level increases.
* How to increase the speed of objects during gameplay.
* How to reset an object's position after completing a level.
* How to create and update a scoreboard.
* How to track game state using Boolean variables.
* How to organize a larger game using multiple classes.
* How to separate the player, cars, and scoreboard into different components.
* How Object-Oriented Programming can make a graphical game easier to organize and maintain.
* How to combine classes, inheritance, lists, loops, events, randomness, and collision detection to create a complete interactive game.

## Challenges

* Understanding how inheritance works.
* Understanding how a child class can inherit functionality from a parent class.
* Understanding the purpose of `super()`.
* Extending the functionality of the `Turtle` class.
* Creating and managing multiple objects from the same class.
* Storing multiple cars in a list.
* Moving every car in the list during each game loop.
* Generating cars at random positions.
* Understanding how random values affect the game.
* Managing the speed of multiple cars.
* Increasing the car speed when the player reaches a new level.
* Detecting collisions between the player and cars.
* Understanding how the `distance()` method can be used for collision detection.
* Detecting when the player reaches the finish line.
* Resetting the player after successfully completing a level.
* Managing the game state while the game is running.
* Connecting keyboard input to player movement.
* Understanding how event listeners work with object methods.
* Updating the scoreboard when the player progresses.
* Organizing the program across multiple classes and modules.
* Keeping the different game components synchronized.
* Debugging the game when objects do not move or respond correctly.
* Understanding how the game loop controls the movement and interaction of multiple objects.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add stronger keyboard input handling.
* Allow the player to move left and right as well as forward.
* Add multiple lanes with different traffic patterns.
* Add different types of vehicles.
* Add different vehicle sizes and speeds.
* Add random car colors.
* Add different road layouts.
* Add obstacles such as road barriers.
* Add power-ups.
* Add bonus points for crossing quickly.
* Add a lives system.
* Add a high-score system.
* Save the player's highest score.
* Add multiple stages or environments.
* Add increasingly difficult traffic patterns.
* Add different background scenes for different levels.
* Add sound effects.
* Add background music.
* Add animations.
* Improve the visual appearance of the road and vehicles.
* Add a countdown before each level.
* Add a pause and resume feature.
* Add a "Play Again?" option after game over.
* Add a start screen and instructions.
* Add a graphical user interface with additional controls.
* Separate the game engine from the graphical interface even further.
* Refactor collision detection into reusable methods.
* Add automated tests for the non-graphical parts of the game.
* Expand the project into a more complete Frogger-style game.
