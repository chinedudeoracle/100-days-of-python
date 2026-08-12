# Day 5 – Password Generator

## Topics Covered

- Lists
- List indexing
- `for` loops
- `range()`
- Random selection with `random.choice()`
- Random number generation with `random.randint()`
- String concatenation
- User input with `input()`
- Converting input to integers with `int()`
- Nested loops
- Building strings dynamically

## Project

### Password Generator

A command-line password generator that creates a random password based on the number of letters, symbols, and numbers requested by the user.

The program randomly selects characters from predefined lists and combines them to create a password.

## How It Works

The user specifies:

1. The number of letters they want.
2. The number of symbols they want.
3. The number of numbers they want.

The program then:

1. Randomly selects the requested number of letters.
2. Randomly selects the requested number of symbols.
3. Randomly selects the requested number of numbers.
4. Combines the selected characters into a password.
5. Displays the generated password.

## Example

```text
Welcome to the PyPassword Generator!

How many letters would you like in your password?
5
How many symbols would you like?
2
How many numbers would you like?
3

Your password is: gTq#m2K$91
```

## What I Learned

- How to use `for` loops to repeat a block of code.
- How to use `range()` to control the number of repetitions.
- How to randomly select items from a list using `random.choice()`.
- How to generate random numbers using `random.randint()`.
- How to build a string dynamically by adding characters to it.
- How to use multiple lists to organize different types of characters.
- How to combine letters, symbols, and numbers to generate a password.
- How nested loops can be used when working with repeated operations.
- How to use user input to determine how many characters should be generated.

## Challenges

- Understanding how `for` loops and `range()` work together.
- Keeping track of how many characters of each type should be generated.
- Understanding how `random.choice()` can be used to select an item from a list.
- Combining characters from different lists into a single password.
- Understanding the difference between generating a password in a fixed order and generating one with randomized character positions.
- Comparing my implementation with the instructor's solution and understanding different ways of solving the same problem.

## Future Improvements

- Ensure that the generated password always contains at least one letter, one symbol, and one number.
- Randomize the final order of all characters in the password.
- Allow the user to specify a minimum and maximum password length.
- Add password strength indicators.
- Allow the user to generate multiple passwords at once.
- Add an option to copy the generated password to the clipboard.
- Add stronger password-generation rules for real-world use.