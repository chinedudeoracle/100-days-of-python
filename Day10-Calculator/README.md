# Day 10 – Calculator

## Topics Covered

- Functions
- Function parameters
- Function arguments
- Keyword arguments
- Returning values from functions with `return`
- Dictionaries
- Dictionary keys and values
- Storing functions in a dictionary
- Retrieving functions from a dictionary
- Calling functions dynamically
- `for` loops
- `if` statements
- User input with `input()`
- Converting input with `int()` and `float()`
- Arithmetic operators
- Variables and assignment
- Building an interactive command-line program

## Project

### Calculator

A command-line calculator that allows the user to perform basic arithmetic operations and continue calculating with the previous result.

The calculator uses separate functions for addition, subtraction, multiplication, and division. These functions are stored in a dictionary and selected dynamically based on the operation chosen by the user.

## How It Works

The program:

1. Asks the user to enter the first number.
2. Displays the available mathematical operations.
3. Asks the user to choose an operation.
4. Asks the user to enter the second number.
5. Uses the selected operation to perform the calculation.
6. Displays the result.
7. Allows the user to choose another operation.
8. Uses the previous result as the first number for the next calculation.
9. Displays the new result.

The program uses a dictionary to associate each mathematical operator with its corresponding function.

For example:

```python
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}
```
## What I Learned

- How to define separate functions for different mathematical operations.
- How to use parameters to pass values into functions.
- How to use `return` to send a calculated value back from a function.
- How to store functions as values in a dictionary.
- How to associate dictionary keys with specific functions.
- How to retrieve a function from a dictionary using a key.
- How to call a function dynamically using a variable.
- How to use keyword arguments when calling functions.
- How to use a `for` loop to display the available operations.
- How to use user input to determine which calculation should be performed.
- How to use arithmetic operators to perform calculations.
- How to use the previous calculation result as the starting point for another calculation.
- How to combine functions, dictionaries, loops, and user input to create an interactive calculator.
- How the same problem can be solved using reusable functions instead of repeating calculation logic.

## Challenges

- Understanding how functions can be stored as values inside a dictionary.
- Understanding the difference between storing a function and calling a function.
- Understanding how `operations[operation_symbol]` retrieves the appropriate function.
- Understanding how a variable such as `calculation_function` can reference different functions.
- Making sure the selected operation is used for each new calculation.
- Identifying a bug where the second calculation continued using the first operation.
- Understanding why `calculation_function` needed to be updated after the user selected another operation.
- Keeping track of the previous calculation result when performing additional operations.
- Understanding how function parameters and keyword arguments work together.

## Future Improvements

- Allow the calculator to work with decimal numbers using `float()`.
- Add input validation for invalid numbers and operations.
- Prevent division by zero.
- Allow the user to continue calculating for as many operations as they want.
- Add a "Start New Calculation" option.
- Add more mathematical operations such as exponentiation and modulus.
- Add functions for square roots, percentages, and other common calculations.
- Improve the user interface and formatting.
- Add a graphical user interface.
- Separate the calculation logic from the user interface even further.
- Add a calculation history.