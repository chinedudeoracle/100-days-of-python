# Day 2 – Tip Calculator

## Topics Covered

- Primitive Data Types
- Numbers (Integers and Floats)
- Type Checking
- Type Conversion
- Mathematical Operations
- Order of Operations (PEMDAS)
- Number Manipulation and F-Strings

## Project

A Python program that calculates how much each person should pay when splitting a restaurant bill, including a chosen tip percentage.

## Example

```text
Welcome to the tip calculator!
What was the total bill? 150.00
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 5

Each person should pay: $33.60
```

## What I Learned

- The difference between `int`, `float`, `str`, and `bool`.
- How to convert between data types using `int()`, `float()`, and `str()`.
- How mathematical operators work in Python.
- The importance of operator precedence (PEMDAS).
- How to round floating-point numbers.
- How to format numbers using f-strings (e.g., `{value:.2f}`).

## Challenges

- Understanding when type conversion is required.
- Remembering that `input()` always returns a string.
- Learning how to format currency to exactly two decimal places.

## Future Improvements

- Validate that the bill amount is greater than zero.
- Validate that the number of people is at least one.
- Allow the user to enter any tip percentage instead of only 10%, 12%, or 15%.
- Handle invalid user input gracefully.