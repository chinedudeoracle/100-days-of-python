# Day 18 – Hirst Painting

## Topics Covered

* Turtle graphics
* The `turtle` module
* Creating and controlling a Turtle object
* Turtle movement
* Coordinates and positioning
* Using `setposition()` to move the Turtle
* `penup()` and `pendown()`
* Drawing dots with `.dot()`
* Setting the Turtle color mode with `colormode()`
* RGB colors
* The `colorgram` module
* Extracting colors from an image
* Working with RGB color values
* Tuples
* Lists
* `random.choice()`
* `for` loops
* `while` loops
* The `range()` function
* Variables and assignment
* Working with external Python packages
* Importing modules
* Using an image as a source for program data
* Building a graphical program
* Automating repetitive drawing tasks

## Project

### Hirst Painting

A Turtle graphics program that recreates the style of Damien Hirst's dot paintings using randomly selected colors extracted from an image.

The program uses the `colorgram` library to extract a collection of colors from a source image. These colors are converted into RGB tuples and stored in a list.

The Turtle then creates a grid of colored dots by randomly selecting a color for each dot.

This project demonstrates how Python can be used to combine image data, randomization, loops, coordinates, and graphical drawing.

## How It Works

The program:

1. Imports the `turtle`, `colorgram`, and `random` modules.
2. Creates a Turtle object.
3. Sets the Turtle color mode to use RGB values from `0` to `255`.
4. Extracts colors from the source image using `colorgram`.
5. Loops through the extracted colors.
6. Retrieves the red, green, and blue values from each color.
7. Stores each RGB color as a tuple in a list.
8. Sets the starting X and Y coordinates for the painting.
9. Creates multiple rows of dots using a `while` loop.
10. Positions the Turtle at the beginning of each row.
11. Uses a `for` loop to create multiple dots across each row.
12. Randomly selects a color from the extracted color list.
13. Draws a colored dot using `.dot()`.
14. Moves the Turtle forward to create spacing between dots.
15. Moves to the next row and repeats the process.
16. Keeps repeating until the required number of rows has been drawn.
17. Keeps the Turtle graphics window open until the user clicks on it.

## Color Extraction

The program uses the `colorgram` package to extract colors from the source image.

```python
extracted_colors = colorgram.extract("./Day18-The-Hirst-Painting/image.jpg", 36)
````

The extracted colors contain RGB information.

The program then converts each extracted color into an RGB tuple:

```python
colors = []

for num in range(0, len(extracted_colors)):
    r = extracted_colors[num].rgb.r
    g = extracted_colors[num].rgb.g
    b = extracted_colors[num].rgb.b

    colors.append((r, g, b))
```

The resulting `colors` list can then be used by Turtle when drawing the dots.

## Creating the Dot Pattern

The painting is created using nested loops.

The outer loop controls the rows, while the inner loop controls the dots within each row.

```python
while count <= 6:
    tim.penup()
    tim.setposition(x_cor, y_cor)
    tim.pendown()

    for _ in range(12):
        turtle_color = random.choice(colors)
        tim.dot(25, turtle_color)

        tim.penup()
        tim.forward(45)
        tim.pendown()

    y_cor += 45
    count += 1
```

For each dot:

1. A random color is selected from the extracted colors.
2. A dot is drawn.
3. The Turtle moves forward.
4. The next dot is drawn.
5. After completing a row, the Turtle moves to the next row.

The program creates a grid containing **7 rows and 12 dots per row**, resulting in **84 dots**.

## Code

```python
import turtle as t
import colorgram
import random


tim = t.Turtle()
t.colormode(255)

extracted_colors = colorgram.extract("./Day18/image.jpg", 36)

colors = []

for num in range(0, len(extracted_colors)):
    r = extracted_colors[num].rgb.r
    g = extracted_colors[num].rgb.g
    b = extracted_colors[num].rgb.b

    colors.append((r, g, b))


x_cor = -240
y_cor = -240
count = 0

while count <= 6:
    tim.penup()
    tim.setposition(x_cor, y_cor)
    tim.pendown()

    for _ in range(12):
        turtle_color = random.choice(colors)
        tim.dot(25, turtle_color)

        tim.penup()
        tim.forward(45)
        tim.pendown()

    y_cor += 45
    count += 1


screen = t.Screen()
screen.exitonclick()
```

## What I Learned

* How to use the `turtle` module to create graphical programs.
* How to create and control a Turtle object.
* How to move a Turtle to specific coordinates.
* How to use `setposition()` to position the Turtle.
* How to use `penup()` and `pendown()` to control whether the Turtle draws while moving.
* How to use `.dot()` to draw circular shapes.
* How to set Turtle's color mode to accept RGB values from `0` to `255`.
* How RGB colors are represented using red, green, and blue values.
* How to install and use an external Python package such as `colorgram`.
* How to use `colorgram.extract()` to extract colors from an image.
* How to access RGB values from extracted colors.
* How to store RGB colors as tuples.
* How to store multiple colors in a list.
* How to use `random.choice()` to randomly select a color.
* How to use `for` loops to repeat a task a specific number of times.
* How to use `while` loops to control repeated drawing operations.
* How to use nested loops to create rows and columns of objects.
* How to use variables to keep track of coordinates.
* How to update the Y coordinate after completing each row.
* How to create consistent spacing between graphical objects.
* How to use an external image as a source of data for a Python program.
* How to combine loops, lists, tuples, randomization, coordinates, and graphical functions into one program.
* How to automate repetitive graphical tasks instead of manually drawing each object.
* How to structure a Python program that interacts with a graphical window.
* How to use an external package installed with `pip` inside a Python project.

## Challenges

* Understanding how the `turtle` module works and how Turtle movement affects the drawing.
* Understanding the coordinate system used by Turtle graphics.
* Positioning the Turtle correctly at the beginning of each row.
* Understanding how `penup()` and `pendown()` affect movement and drawing.
* Understanding how to use `.dot()` to create the individual circles.
* Understanding how RGB colors are represented as tuples.
* Understanding how to extract color information from an image using `colorgram`.
* Accessing the RGB attributes of the colors returned by `colorgram`.
* Converting the extracted RGB values into tuples that Turtle can use.
* Storing the extracted colors in a list.
* Using `random.choice()` to select a different color for each dot.
* Understanding how nested loops can be used to create a grid.
* Keeping the spacing between dots consistent.
* Keeping track of the X and Y coordinates while moving between rows.
* Understanding how the outer loop controls the rows and the inner loop controls the dots.
* Determining the appropriate number of rows and columns for the painting.
* Combining an external Python package with the standard Python library.
* Debugging the program when the graphical output does not appear as expected.
* Understanding how to automate a visual pattern using loops instead of manually positioning every dot.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Use a `for` loop instead of a `while` loop for controlling the number of rows.
* Define constants for the number of rows, columns, dot size, and spacing.
* Refactor the color extraction into a separate function.
* Refactor the dot-grid drawing into a separate function.
* Improve the positioning logic to center the painting automatically.
* Allow the user to choose the size of the painting.
* Allow the user to choose the number of rows and columns.
* Allow the user to choose the size and spacing of the dots.
* Extract colors from different source images.
* Remove colors that are too dark or too light.
* Prevent similar colors from being selected too frequently.
* Add more sophisticated color-selection logic.
* Generate different dot patterns and layouts.
* Add multiple shapes instead of only circular dots.
* Allow the user to save the generated painting as an image.
* Add a graphical user interface for controlling the painting.
* Create an animation showing the painting being drawn.
* Experiment with different Turtle drawing speeds.
* Create a reusable painting generator that can work with different images.

