# Day 25 – Working with CSV Data and the Pandas Library

## Topics Covered

- Introduction to CSV files
- What CSV (Comma Separated Values) files are
- Why CSV is a common data format
- Reading CSV files using Python's built-in `csv` module
- Reading CSV files using the `pandas` library
- The `pandas` library and why it is used for data analysis
- Installing and importing `pandas`
- Creating a `DataFrame` from a CSV file
- Understanding `DataFrame` and `Series` objects
- Viewing data with `head()`, `tail()`, and `sample()`
- Getting the shape and dimensions of a `DataFrame`
- Accessing columns by name
- Selecting single and multiple columns
- Accessing rows using index positions
- Filtering data with conditional expressions
- Converting `DataFrame` columns to lists with `to_list()`
- Extracting single values with `.item()`
- Writing data to a CSV file with `to_csv()`
- Handling user input with `.lower()` and `.strip()`
- Combining `pandas` with `turtle` graphics
- Separating data logic from presentation logic
- Tracking game state and user progress
- Generating output files for further study

## Project

### Nigerian States Game

An interactive geography quiz game that uses `pandas` to read and manage Nigerian state data from a CSV file.

Instead of following the instructor's US States Game, I adapted the project to build a **Nigerian States Game** using a custom `37_states.csv` dataset containing Nigerian state names and their x/y coordinates.

The program displays a blank map of Nigeria and prompts the user to guess the names of all 37 states (36 states + the FCT). When the user types a correct state name, the state's name is written onto the map at its correct position. The game continues until the user guesses all 37 states or exits the game.

The program:

1. Reads a CSV file containing Nigerian state names and their x/y coordinates.
2. Stores the data in a `pandas` `DataFrame`.
3. Displays a blank map of Nigeria.
4. Prompts the user to enter a state name.
5. Normalizes the input using `.lower()` and `.strip()`.
6. Checks whether the guessed state exists in the `DataFrame`.
7. If correct, writes the state name onto the map at its coordinates.
8. Tracks which states have already been guessed.
9. Tracks the number of correct guesses.
10. Allows the user to exit early by typing "Exit".
11. Saves the list of states the user missed to a `states_to_learn.csv` file.

This demonstrates how `pandas` can be used to manage structured data and how that data can be combined with graphical output.

## How It Works

The program:

1. Imports the required modules (`turtle`, `pandas`).
2. Reads the `37_states.csv` file into a `DataFrame`.
3. Creates the game screen and sets the background image to the Nigerian map.
4. Enters a `while` loop that continues until all 37 states are guessed.
5. Prompts the user for a state name using `screen.textinput()`.
6. Normalizes the input using `.lower()` and `.strip()`.
7. If the user types "exit", ends the game and saves the missed states.
8. Loops through the `DataFrame` to check whether the guessed state exists.
9. If correct and not already guessed, adds the state to the guessed list.
10. Creates a turtle to write the state name onto the map at its coordinates.
11. Updates the title to show the current score.
12. Ends the game when all 37 states have been guessed.
13. Writes any unguessed states to a `states_to_learn.csv` file for further study.

## File Structure

The project uses the following file structure:

```
Day25-Working-with-CSV-Data-and-the-Pandas-Library/
│
├── 37_states.csv
├── nigeria-map.gif
├── states_to_learn.csv
└── main.py
```

The `37_states.csv` file contains the Nigerian state names and their x/y coordinates. The `nigeria-map.gif` file is the map image displayed during the game. The `states_to_learn.csv` file is generated at the end of the game and contains the states the user did not guess.

## Working with CSV Files

### Reading a CSV File with `pandas`

```python
import pandas

nigerian_states_df = pandas.read_csv("37_states.csv")
```

This reads the CSV file into a `DataFrame`, which is a tabular data structure similar to a spreadsheet.

### Accessing a Column

```python
state_names = nigerian_states_df.State.to_list()
```

This extracts all values from the `State` column and converts them into a Python list.

### Getting the Number of Rows

```python
nigerian_states_df.State.size
```

This returns the number of entries in the `State` column, which is used to determine when the game is complete.

### Accessing Values by Position

```python
nigerian_states_df.State[num]
nigerian_states_df.x[num]
nigerian_states_df.y[num]
```

This retrieves the state name and its coordinates at position `num` in the `DataFrame`.

## Pandas Basics

### Creating a `DataFrame`

```python
import pandas

data = {
    "name": ["Abia", "Adamawa", "Akwa Ibom"],
    "x": [100, 200, 300],
    "y": [50, 60, 70]
}

df = pandas.DataFrame(data)
```

### Selecting Columns

```python
df["State"]
df[["State", "x"]]
```

### Filtering Rows

```python
df[df["State"] == "Lagos"]
```

### Writing to a CSV File

```python
missed_states_df = pandas.DataFrame(missed_states, columns=["State"])
missed_states_df.to_csv("states_to_learn.csv")
```

## User Input Handling

User input is normalized to make matching more forgiving:

```python
answer_state = screen.textinput(
    title=title,
    prompt="What's another state's name?"
).lower().strip()
```

- `.lower()` handles case insensitivity (e.g., "lagos" matches "Lagos").
- `.strip()` removes accidental leading or trailing whitespace.

This is more robust than the instructor's approach, which used `.title()` and did not handle whitespace.

## Code

### Main Program

```python
import pandas
import turtle


screen = turtle.Screen()
screen.title("Nigerian States Game")
image = "./Day25-Working-with-CSV-Data-and-the-Pandas-Library/nigeria-map.gif"
screen.addshape(image)
turtle.shape(image)


nigerian_states_df = pandas.read_csv(
    "./Day25-Working-with-CSV-Data-and-the-Pandas-Library/37_states.csv"
)

title = "Guess the State"
guessed_states = []

while len(guessed_states) < 37:
    answer_state = screen.textinput(
        title=title, prompt="What's another state's name?"
    ).lower().strip()

    if answer_state == "exit":
        missed_states = []
        for state in nigerian_states_df.State.str.lower():
            if state not in guessed_states:
                missed_states.append(state)
        missed_states_df = pandas.DataFrame(missed_states, columns=["State"])
        missed_states_df.to_csv(
            "./Day25-Working-with-CSV-Data-and-the-Pandas-Library/states_to_learn.csv"
        )
        break

    for num in range(nigerian_states_df.State.size):
        if (
            answer_state == nigerian_states_df.State[num].lower()
            and answer_state not in guessed_states
        ):
            guessed_states.append(answer_state)
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.pencolor("black")
            new_turtle.goto(
                nigerian_states_df.x[num], nigerian_states_df.y[num]
            )
            new_turtle.write(nigerian_states_df.State[num])
            title = f"{len(guessed_states)}/37 States Correct"


turtle.mainloop()
```

## What I Learned

- What CSV files are and why they are widely used.
- How to read CSV files using the `pandas` library.
- How to create a `DataFrame` from a CSV file.
- The difference between a `DataFrame` and a `Series`.
- How to access columns by name.
- How to convert a `DataFrame` column to a Python list using `to_list()`.
- How to get the size of a column using `.size`.
- How to access values by position in a `DataFrame`.
- How to filter and iterate over data.
- How to extract single values from a `DataFrame`.
- How to write a `DataFrame` to a CSV file using `to_csv()`.
- How to combine `pandas` with other libraries like `turtle`.
- How to normalize user input with `.lower()` and `.strip()`.
- How to handle case-insensitive matching.
- How to track user progress and provide feedback.
- How to generate a useful output file for further study.
- How to adapt a tutorial project to a different domain (Nigerian states).
- How to build an interactive game that uses real data.
- How to separate data logic from presentation logic.

## Challenges

- Adapting the instructor's US States Game to a Nigerian context.
- Sourcing or creating a suitable CSV dataset with state coordinates.
- Aligning state names in the CSV with the map image.
- Understanding how `pandas` indexes data.
- Understanding when to use positional indexing versus filtering.
- Checking whether a value exists in a list.
- Avoiding duplicate guesses.
- Handling case-insensitive input matching.
- Handling whitespace in user input.
- Managing game state across multiple iterations of a loop.
- Writing state names to the correct map coordinates.
- Combining `pandas` data with `turtle` graphics.
- Saving the list of missed states to a new CSV file.
- Understanding the full workflow of a data-driven interactive program.
- Comparing my own implementation with the instructor's solution.
- Recognizing where my implementation improved on the instructor's approach (input handling).
- Recognizing where my implementation could be improved further (single turtle instance, `None` input handling, boolean filtering).

## Future Improvements

- Handle `None` input when the user cancels the dialog.
- Create a single turtle writer instance instead of one per guess.
- Preserve original state casing in the `states_to_learn.csv` output.
- Replace positional indexing with boolean filtering for robustness.
- Add support for countries instead of Nigerian states.
- Add support for different map images and datasets.
- Add a timer to track how long the game takes.
- Add a hint system that reveals the first letter of a state.
- Add a difficulty mode that hides the score.
- Add a "Play Again?" option after the game ends.
- Add a start screen with instructions.
- Add sound effects for correct and incorrect guesses.
- Add a graphical user interface using Tkinter.
- Add support for reading data from an API instead of a CSV file.
- Add support for multiple data sources.
- Add data visualization using `matplotlib` or `seaborn`.
- Add the ability to export results to different formats (Excel, JSON).
- Add unit tests for the data processing logic.
- Refactor the program into reusable functions.
- Create a class-based version of the game.
- Add logging to track user progress.
- Add performance improvements for large datasets.
- Add support for multiple languages.
- Add support for online leaderboards.
