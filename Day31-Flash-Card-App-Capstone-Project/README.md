# Day 31 – Flash Card App Capstone Project

## Topics Covered

* Python
* Tkinter
* Graphical User Interfaces (GUI)
* Creating a desktop application
* Tkinter `Canvas`
* `PhotoImage`
* Tkinter `Button`
* Tkinter `Label`
* Tkinter `Entry`
* Widget configuration
* Widget positioning with `.grid()`
* Widget positioning with `.place()`
* Event-driven programming
* Functions as button commands
* Dictionaries
* Lists
* List indexing
* Dictionary keys and values
* Working with CSV files
* Reading CSV data with Pandas
* Creating Pandas DataFrames
* Converting DataFrame columns to lists
* Random selection with `random.choice()`
* Removing items from lists
* Working with program state
* Boolean values
* Conditional statements
* `if` statements
* `else` statements
* `after()` for scheduled GUI events
* Callback functions
* File paths
* Working with external data files
* Separating application data from program logic
* Building an interactive GUI application
* Building a complete Python capstone project

## Project

### Flash Card App

A graphical flash card application designed to help users learn vocabulary by displaying words in one language and allowing the user to recall their translation.

The application displays a word on a flash card and automatically flips the card after a short period of time to reveal the translation.

The user can then indicate whether they knew the answer.

Words that the user does not know remain available for future practice, while words that have been learned can be removed from the current learning set.

The application uses a CSV file as its source of vocabulary data and uses Pandas to load and process the data.

The project combines Python programming, data processing, GUI development, random selection, and event-driven programming into a complete desktop application.

## How It Works

The program:

1. Loads the vocabulary data from a CSV file.
2. Processes the vocabulary data using Pandas.
3. Converts the relevant data into a structure that can be used by the application.
4. Randomly selects a word to display.
5. Displays the word on the front of the flash card.
6. Waits for a short period of time.
7. Automatically flips the card.
8. Displays the translation on the back of the card.
9. Allows the user to indicate whether they knew the word.
10. Removes learned words from the current learning data when appropriate.
11. Selects another word.
12. Continues the learning process until the available words have been completed.

## Flash Card Interface

The application uses Tkinter to create the graphical interface.

The interface contains:

- A flash card displaying the current word.
- A front side showing the word to learn.
- A back side showing the translation.
- A button for indicating that the word was known.
- A button for indicating that the word was not known.

The flash card is created using a Tkinter `Canvas` and image files.

## Working with CSV Data

The vocabulary data is stored in a CSV file.

Pandas can be used to load the CSV file:

```python
import pandas

data = pandas.read_csv("./Day31/data/french_words.csv")
````

The resulting DataFrame can then be used to access the vocabulary columns.

For example:

```python
word_list = data.to_dict(orient="records")
```

This converts the data into a list of dictionaries that can be easily processed by the application.

## Random Word Selection

The application randomly selects a word from the available vocabulary.

```python
from random import choice

current_card = choice(word_list)
```

This allows the flash cards to appear in a different order rather than always following the order of the CSV file.

## Removing Learned Words

When the user indicates that a word has been learned, the application can remove that word from the current learning data.

This prevents words that the user already knows from repeatedly appearing during the same learning session.

The remaining vocabulary can also be saved so that the user's progress can be preserved.

## Automatic Card Flipping

The application uses Tkinter's `after()` method to schedule an action after a specified amount of time.

For example:

```python
window.after(3000, flip_card)
```

This allows the program to display the front of the card and then automatically execute the `flip_card()` function after the specified delay.

This demonstrates how GUI programs can perform actions based on time without blocking the main event loop.

## Event-Driven Programming

Unlike a command-line program that normally executes from top to bottom, a GUI application waits for events.

Examples of events in this project include:

* The user clicking the "known" button.
* The user clicking the "unknown" button.
* The timer reaching the specified delay.
* The application window being created and displayed.

Functions are connected to these events so that the appropriate code runs when the event occurs.

For example:

```python
Button(command=next_card)
```

The function is passed as the command rather than being executed immediately.

## Code Structure

The project can be organized around several functions responsible for different parts of the application.

### `next_card()`

Responsible for:

* Selecting another word.
* Updating the flash card.
* Displaying the word.
* Scheduling the card flip.

### `flip_card()`

Responsible for:

* Changing the flash card image.
* Changing the text displayed on the card.
* Showing the translation.

### `is_known()`

Responsible for:

* Recording that the user knows the current word.
* Removing the learned word from the current learning data.
* Moving to the next card.

Separating these responsibilities into functions makes the program easier to understand and maintain.

## What I Learned

* How to build a complete graphical application using Tkinter.
* How to create and configure Tkinter widgets.
* How to use `Canvas` to create a graphical flash card.
* How to use `PhotoImage` to display images.
* How to use buttons to trigger functions.
* How to use functions as callback commands.
* How GUI applications are driven by user events.
* How to use `.grid()` and `.place()` to position widgets.
* How to load data from a CSV file.
* How to use Pandas to work with CSV data.
* How to convert a DataFrame into a list of dictionaries.
* How to access dictionary keys and values.
* How to use lists to store and manipulate vocabulary data.
* How to randomly select an item using `random.choice()`.
* How to remove items from a list.
* How to maintain the state of an application while it is running.
* How to use conditional statements to control program behavior.
* How to use Tkinter's `after()` method to schedule a function.
* How callback functions work in GUI applications.
* How to separate application data from application logic.
* How to combine data processing and GUI programming in one application.
* How to build a practical application from several previously learned Python concepts.
* How to organize a larger Python project into separate functions and components.
* How to build a complete Python capstone project from start to finish.

## Challenges

* Understanding how Tkinter manages GUI events.
* Understanding how callback functions work with buttons.
* Understanding why a callback function should be passed without parentheses.
* Working with Tkinter's `Canvas` widget.
* Positioning text and images correctly on the flash card.
* Managing different images for the front and back of the card.
* Loading vocabulary data from a CSV file.
* Understanding the structure of a Pandas DataFrame.
* Converting Pandas data into a list of dictionaries.
* Accessing values stored inside dictionaries.
* Randomly selecting vocabulary items.
* Keeping track of the current flash card.
* Removing learned words from the available vocabulary.
* Managing the state of the application as the user progresses.
* Understanding how `after()` schedules a function to run later.
* Coordinating the card display with the automatic card flip.
* Making sure the correct word and translation are displayed.
* Connecting multiple functions together to create the complete application.
* Managing file paths for images and data files.
* Debugging the application when the GUI does not behave as expected.
* Combining previously learned Python concepts into a larger project.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add more languages besides French.
* Allow the user to select the language being studied.
* Allow the user to import their own vocabulary.
* Add a feature for creating custom flash card sets.
* Add multiple vocabulary categories.
* Add difficulty levels.
* Track the number of words learned.
* Track the user's progress over time.
* Save learning progress between sessions.
* Add a progress indicator.
* Add a daily learning goal.
* Add statistics showing known and unknown words.
* Add a review system for words that are difficult to remember.
* Increase the frequency of difficult words.
* Add pronunciation audio.
* Add text-to-speech functionality.
* Add example sentences for each word.
* Add images associated with vocabulary words.
* Add keyboard shortcuts for marking cards as known or unknown.
* Add a restart or reset learning-session option.
* Improve the graphical design of the flash cards.
* Add animations when flipping cards.
* Create multiple study modes.
* Store vocabulary and progress in a database.
* Add automated tests for the application's non-GUI logic.
* Package the application as a standalone desktop application.

## Project Reflection

This project brought together many of the Python concepts learned during the previous days of the course.

Instead of building a small isolated exercise, the Flash Card App required combining:

* Python data structures
* CSV data
* Pandas
* Random selection
* Functions
* Dictionaries
* Lists
* Tkinter
* GUI widgets
* Event-driven programming
* Timed callbacks
* File handling

The project demonstrates how individual Python concepts can be combined to create a practical application.

It also provided additional experience working with external data and building a graphical user interface that responds to user interaction.
