# Day 8 – Caesar Cipher

## Topics Covered

- Functions
- Function parameters
- Function arguments
- `for` loops
- `if` and `elif` statements
- Lists
- List indexing
- String manipulation
- User input with `input()`
- String methods such as `.lower()`
- Combining strings
- The `range()` function
- Modular arithmetic
- Encoding and decoding
- Building an interactive command-line program

## Project

### Caesar Cipher

A command-line Caesar Cipher program that allows the user to encode and decode messages by shifting each letter of the alphabet by a specified number of positions.

The program uses a shift value to move each letter forward when encoding and backward when decoding.

## How It Works

The program:

1. Asks the user whether they want to encode or decode a message.
2. Asks the user to enter the message.
3. Asks the user to enter the shift number.
4. Processes each letter in the message.
5. Shifts each letter by the specified number of positions.
6. Keeps spaces and characters that are not part of the alphabet unchanged.
7. Displays the encoded or decoded message.
8. Allows the user to continue using the program or exit.

The program uses the alphabet stored in a list and calculates the new position of each letter based on the shift number.

## Code

```python
def caesar(start_text, shift_amount, cipher_direction):
    # Encode or decode the message
    # by shifting each letter in the alphabet.
    pass
```
## What I Learned

- How to define functions with parameters.
- How function parameters allow the same function to work with different values.
- How to use `for` loops to process each character in a string.
- How to use list indexing to find and manipulate individual letters.
- How to use the `range()` function to work with a sequence of numbers.
- How to use `if` and `elif` statements to handle different program conditions.
- How to use user input to determine whether a message should be encoded or decoded.
- How to manipulate strings by building a new string from individual characters.
- How to use modular arithmetic to make the alphabet wrap around when the shift goes beyond `Z`.
- How encoding and decoding can use the same function with different shift directions.
- How to handle characters that are not included in the alphabet.
- How to build an interactive encryption and decryption program using Python.

## Challenges

- Understanding how the position of each letter in the alphabet can be changed using a shift number.
- Understanding how to make the alphabet wrap around when the shift goes beyond the end of the list.
- Understanding how modular arithmetic can solve the alphabet wrap-around problem.
- Structuring the function so that it can handle both encoding and decoding.
- Keeping spaces and other characters unchanged.
- Understanding how function parameters and arguments work together.
- Keeping track of the different variables used for the message, shift amount, and direction.
- Understanding how to process each character of a message individually.
- Making sure the correct shift direction is used when encoding versus decoding.

## Future Improvements

- Add stronger input validation for the shift number.
- Prevent invalid characters from causing unexpected results.
- Allow the user to repeatedly encode and decode messages without restarting the program.
- Add an option to automatically detect whether a message is encoded.
- Add a graphical user interface.
- Allow users to encrypt and decrypt text from a file.
- Add additional encryption techniques beyond the Caesar Cipher.
- Compare the Caesar Cipher with more advanced encryption methods.
- Add a message history so previous encoded and decoded messages can be viewed.