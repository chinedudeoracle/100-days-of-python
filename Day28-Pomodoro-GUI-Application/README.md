# Day 28 – Pomodoro GUI Application

## Topics Covered

* Tkinter
* Graphical User Interfaces (GUI)
* Creating GUI applications with Python
* Creating and configuring a `Tk()` window
* Labels
* Buttons
* Canvas widgets
* Images in Tkinter
* `PhotoImage`
* Using `.grid()` to position widgets
* Widget configuration
* Using `.config()` to update widgets
* Button callbacks
* Event-driven programming
* Functions
* Global variables
* Constants
* Working with time
* The `time` module
* `countdown()` functions
* Using `after()` for scheduled function calls
* Recursive function calls
* Converting seconds into minutes and seconds
* String formatting
* F-strings
* Dynamic typing
* Understanding Python's dynamic type system
* Type inference at runtime
* Variable reassignment
* Using different data types with the same variable
* Managing application state
* Building a timer application
* Creating a Pomodoro timer
* Resetting application state
* Tracking work and break intervals
* Automating repeated tasks
* Combining GUI components with program logic

## Project

### Pomodoro Timer

A graphical Pomodoro timer application built with Tkinter.

The application uses the Pomodoro Technique to divide work into focused sessions followed by short breaks and longer breaks after several work sessions.

The user can start the timer and the application automatically progresses through work sessions and break periods.

The interface displays the current timer, indicates whether the user is working or taking a break, and keeps track of completed work sessions using check marks.

The project demonstrates how Python can be used to create a complete interactive GUI application while combining Tkinter, functions, timers, variables, and program state.

## How It Works

The program:

1. Creates the main Tkinter window.
2. Configures the window and its layout.
3. Creates the timer title and display.
4. Creates a Canvas widget for displaying the tomato image.
5. Creates Start and Reset buttons.
6. Defines the Pomodoro timing constants.
7. Keeps track of the number of completed work sessions.
8. Starts the countdown when the user clicks **Start**.
9. Determines whether the next interval is a work session or a break.
10. Converts the selected duration from minutes into seconds.
11. Updates the timer display every second.
12. Uses Tkinter's `after()` method to schedule the next countdown update.
13. Changes the timer title depending on the current session.
14. Adds a check mark when a work session is completed.
15. Automatically starts the next session when the current countdown reaches zero.
16. Uses longer breaks after a set number of work sessions.
17. Allows the user to reset the timer and return the application to its initial state.

## Pomodoro Timing System

The application uses three different timer durations:

* **Work:** 25 minutes
* **Short Break:** 5 minutes
* **Long Break:** 20 minutes

The work and break durations are stored as constants:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

The application determines which duration to use based on the number of completed work sessions.

The general pattern is:

```text
Work → Short Break → Work → Short Break → Work → Short Break → Work → Long Break
```

This cycle then repeats.

## Timer Countdown

The countdown is handled by a function that receives the remaining number of seconds.

Conceptually:

```python
def count_down(count):
    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        window.after(1000, count_down, count - 1)
```

The `after()` method schedules the function to run again after a specified amount of time.

In this case:

```python
window.after(1000, count_down, count - 1)
```

means that Tkinter waits approximately 1,000 milliseconds before calling `count_down()` again with the updated value.

This creates the countdown effect without blocking the GUI.

## Using the Canvas

The Canvas widget is used to display the tomato image and timer text.

For example:

```python
canvas = Canvas(
    width=200,
    height=224
)
```

An image can be loaded using:

```python
tomato_img = PhotoImage(file="tomato.png")
```

The image can then be placed on the Canvas.

The timer text can also be displayed on the Canvas and updated during the countdown.

## Updating the Timer Display

The timer text can be changed using:

```python
canvas.itemconfig(
    timer_text,
    text="25:00"
)
```

This allows the same Canvas text object to be updated every second rather than creating a new text object each time.

## Dynamic Typing

Python uses **dynamic typing**, meaning that variables do not need to have their data type explicitly declared.

For example:

```python
value = 10
```

Here, `value` refers to an integer.

The same variable can later refer to a string:

```python
value = "Hello"
```

Python determines the type of the object at runtime.

This is different from statically typed languages where a variable's type is generally declared or constrained.

Dynamic typing makes Python flexible, but it also means that the programmer needs to be aware of the types of values being used.

## Code

A simplified version of the main timer logic:

```python
import tkinter


WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0


def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
    else:
        count_down(WORK_MIN * 60)


def count_down(count):
    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(
        timer_text,
        text=f"{minutes:02d}:{seconds:02d}"
    )

    if count > 0:
        window.after(
            1000,
            count_down,
            count - 1
        )


window = tkinter.Tk()

canvas = tkinter.Canvas(
    width=200,
    height=224
)

timer_text = canvas.create_text(
    100,
    112,
    text="25:00"
)

canvas.pack()

window.mainloop()
```

The actual project combines this timer logic with the complete Tkinter interface, images, buttons, labels, session tracking, and reset functionality.

## What I Learned

* How to build a more complete GUI application using Tkinter.
* How to create and configure a Tkinter window.
* How to create Labels, Buttons, and Canvas widgets.
* How to use `PhotoImage` to work with images in Tkinter.
* How to use Canvas to display images and text.
* How to update Canvas objects using `.itemconfig()`.
* How to connect buttons to functions using callbacks.
* How to use `grid()` to organize GUI widgets.
* How to use constants to store values that should remain unchanged.
* How to organize a program around application state.
* How to use the `time` concept of minutes and seconds in a countdown.
* How to convert minutes into seconds for timer calculations.
* How integer division with `//` can be used to calculate minutes.
* How the modulo operator `%` can be used to calculate remaining seconds.
* How to format numbers using f-strings.
* How to display leading zeros using formatting such as `:02d`.
* How to use Tkinter's `after()` method to schedule a function.
* How scheduled function calls can be used to create a countdown timer.
* How recursive function calls can be used to continue the countdown.
* How to automatically transition between work sessions and breaks.
* How to keep track of completed Pomodoro sessions.
* How to determine when to use a short break or a long break.
* How to update GUI elements while a program is running.
* How to reset the state of an application.
* How event-driven programming can be used to create interactive applications.
* How Python's dynamic typing works.
* How a variable can refer to objects of different types during program execution.
* How Python determines types at runtime.
* How dynamic typing provides flexibility when writing Python programs.
* How to combine GUI programming, functions, timers, variables, and program state into a complete application.

## Challenges

* Understanding how Tkinter's event loop works.
* Understanding how `after()` schedules a function without blocking the GUI.
* Understanding how the countdown function repeatedly calls itself.
* Converting between minutes and seconds correctly.
* Understanding integer division and the modulo operator when working with time.
* Formatting the timer so that seconds always display with two digits.
* Keeping the timer display synchronized with the countdown value.
* Understanding how the program determines whether the current interval is a work session or a break.
* Tracking the number of completed sessions using the `reps` variable.
* Understanding the logic for determining when a long break should occur.
* Updating different parts of the GUI as the timer progresses.
* Adding check marks after completed work sessions.
* Understanding how the Reset button needs to restore the application's state.
* Managing global variables that are shared between functions.
* Understanding how Canvas objects are created and updated.
* Working with images inside a Tkinter Canvas.
* Understanding how dynamic typing works in Python.
* Understanding that Python variables do not have a fixed declared type.
* Debugging the timer when the countdown does not update or transition correctly.
* Combining several functions so that they work together as one application.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Allow the user to customize the work duration.
* Allow the user to customize the short-break duration.
* Allow the user to customize the long-break duration.
* Add a settings screen for changing timer durations.
* Add a pause button.
* Add a resume button.
* Add a skip-session button.
* Add a confirmation before resetting the timer.
* Display the current session number.
* Display the number of completed Pomodoro sessions.
* Save completed sessions between application launches.
* Add daily productivity statistics.
* Add weekly productivity statistics.
* Add a task list so users can associate Pomodoro sessions with specific tasks.
* Add notifications when a session ends.
* Add sound effects for completed sessions.
* Allow the user to choose different notification sounds.
* Add different themes.
* Add dark mode.
* Improve the visual design of the application.
* Make the window responsive.
* Add keyboard shortcuts.
* Add pause/resume support without losing the current countdown value.
* Separate the timer logic from the GUI logic.
* Create a reusable timer class.
* Add automated tests for the timer logic.
* Store user settings in a configuration file.
* Build a more complete personal productivity application around the Pomodoro technique.
