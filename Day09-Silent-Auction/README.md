# Day 9 – Silent Auction

## Topics Covered

- Dictionaries
- Dictionary keys and values
- Adding and updating dictionary entries
- Functions
- Function parameters
- Function arguments
- Keyword arguments
- `for` loops
- `while` loops
- Conditional statements (`if`, `else`)
- Comparison operators
- User input with `input()`
- String methods such as `.lower()`
- Boolean variables
- Tracking program state
- Finding the highest value in a collection
- Importing modules
- Clearing the terminal with `os.system()`
- Building an interactive command-line program

## Project

### Silent Auction

A command-line silent auction program that allows multiple bidders to enter their names and bids.

The program stores each bidder and their bid in a dictionary, continues accepting bids until there are no more bidders, and then determines the bidder with the highest bid.

## How It Works

The program:

1. Displays the auction logo.
2. Asks the user to enter their name.
3. Asks the user to enter their bid amount.
4. Stores the bidder's name and bid in a dictionary.
5. Asks whether there are any other bidders.
6. Clears the terminal if another bidder wants to participate.
7. Continues accepting bids until there are no more bidders.
8. Loops through the dictionary to find the highest bid.
9. Displays the winner and their winning bid.

The program uses separate functions to add bidders and determine the highest bidder.

## Code

```python
bidders = {}

def add_new_bidder(bidder_name, bid_amount):
    bidders[bidder_name] = bid_amount

def find_highest_bidder(bid_record):
    highest_bid = 0
    highest_bidder = ''

    for bidder in bid_record:
        bid_amount = bid_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
```
## What I Learned

- How to use dictionaries to store related data using key-value pairs.
- How to add new key-value pairs to a dictionary.
- How to define functions with parameters.
- How function parameters allow functions to work with different values.
- How to use function arguments when calling a function.
- How to use keyword arguments when calling a function.
- How to use `for` loops to go through the contents of a dictionary.
- How to use a `while` loop to keep the auction running while there are additional bidders.
- How to use conditional statements to control the flow of the program.
- How to use comparison operators to determine which bid is the highest.
- How to keep track of the highest value while looping through a collection.
- How to use a Boolean variable to control the state of a `while` loop.
- How to use `.lower()` to make the user's response case-insensitive.
- How to use `os.system("cls")` to clear the Windows terminal between bidders.
- How to separate different parts of a program into reusable functions.
- How to build an interactive program using dictionaries, functions, loops, and conditional logic.

## Challenges

- Understanding how to store each bidder's name and bid using a dictionary.
- Understanding how dictionary keys and values work together.
- Passing information into functions using parameters and arguments.
- Understanding how to loop through a dictionary to access each bidder and their bid.
- Keeping track of the highest bid while checking multiple bidders.
- Making sure the correct bidder is stored whenever a new highest bid is found.
- Using a `while` loop to continue accepting bids until the auction ends.
- Understanding how a Boolean variable can be used to control the `while` loop.
- Managing the flow of the program when the user chooses whether or not there are additional bidders.
- Understanding how to separate the program into functions rather than placing all the logic in one block of code.

## Future Improvements

- Add input validation for bid amounts.
- Prevent users from entering negative or invalid bid amounts.
- Handle situations where two bidders enter the same highest bid.
- Display a message when there is a tie.
- Allow the user to see the list of bidders after the auction ends.
- Add a minimum bid amount.
- Add a "Play Again?" or "Start New Auction?" option.
- Store auction results in a file.
- Allow multiple auctions to be conducted during the same program session.
- Improve the terminal-clearing function so the program works on Windows, macOS, and Linux.
- Separate the auction logic from the user interface even further by having functions return values instead of printing results directly.