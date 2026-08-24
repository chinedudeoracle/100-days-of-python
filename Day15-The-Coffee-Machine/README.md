# Day 15 – Coffee Machine

## Topics Covered

* Dictionaries
* Nested dictionaries
* Dictionary keys and values
* Accessing values from nested dictionaries
* Functions
* Function parameters and arguments
* `return` statements
* `for` loops
* `while` loops
* Conditional statements (`if`, `elif`, `else`)
* Boolean values
* Comparison operators
* Logical thinking and program flow
* User input with `input()`
* String methods such as `.lower()` and `.strip()`
* Arithmetic operations
* Formatting numbers with f-strings
* Working with program state
* Managing and updating resources
* Processing coins and calculating payments
* Checking whether sufficient resources are available
* Building reusable functions
* Organizing data separately from program logic
* Building an interactive command-line program

## Project

### Coffee Machine

A command-line coffee machine program that allows users to purchase different types of coffee.

The program offers espresso, latte, and cappuccino. Each drink requires specific amounts of water, coffee, and, in some cases, milk. The program also keeps track of available resources and the money earned from successful transactions.

Users can request a report showing the machine's current resources or turn the machine off.

## How It Works

The program:

1. Stores the ingredients required for each type of coffee.
2. Stores the price of each coffee.
3. Stores the machine's available resources.
4. Stores the values of the different types of coins.
5. Asks the user what type of coffee they would like.
6. Allows the user to enter `report` to view the current resources.
7. Allows the user to enter `off` to shut down the machine.
8. Checks whether there are enough resources to make the selected coffee.
9. Asks the user to enter the required coins.
10. Calculates the total amount of money inserted.
11. Checks whether the payment is sufficient.
12. Calculates and returns change when necessary.
13. Adds the price of the coffee to the machine's money.
14. Deducts the required ingredients from the available resources.
15. Dispenses the selected coffee.
16. Continues running until the user enters `off`.

The program uses dictionaries and nested dictionaries to store the coffee recipes, prices, resources, and coin values.

## Code

```python
FLAVOURS = {
    "espresso": {"water": 50, "coffee": 18},
    "latte": {"water": 200, "coffee": 24, "milk": 150},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100},
}

PRICES = {
    "espresso": 1.50,
    "latte": 2.50,
    "cappuccino": 3.00,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources_sufficient(flavour):
    for resource in FLAVOURS[flavour]:
        if FLAVOURS[flavour][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def make_coffee(choice):
    for resource in FLAVOURS[choice]:
        resources[resource] -= FLAVOURS[choice][resource]

    print(f"Here is your {choice} ☕ Enjoy!")
```

## What I Learned

* How to use dictionaries to store related data using key-value pairs.
* How to use nested dictionaries to represent more complex data.
* How to access values from nested dictionaries using multiple keys.
* How to define functions that perform specific tasks.
* How to use function parameters and arguments to make functions reusable.
* How to use `return` to send values back from functions.
* How to use `for` loops to process the resources required for each coffee.
* How to use `while` loops to keep the coffee machine running.
* How to use conditional statements to control the flow of the program.
* How to use Boolean values such as `True` and `False` to control program logic.
* How to compare required resources with available resources.
* How to process different types of coins and calculate their monetary value.
* How to calculate change using arithmetic operations.
* How to update resources after a successful transaction.
* How to keep track of the money earned by the machine.
* How to use `.lower()` and `.strip()` to process user input.
* How to use f-strings to display dynamic messages and formatted currency.
* How to use dictionary membership with `in` to check whether a user choice is valid.
* How to separate different parts of a program into reusable functions.
* How to organize program data separately from the logic that operates on that data.
* How to build an interactive command-line program that maintains state while running.

## Challenges

* Understanding how nested dictionaries can be used to represent coffee recipes.
* Accessing the correct resources from nested dictionaries.
* Understanding how to check every required resource before making a coffee.
* Debugging an issue caused by returning `True` from inside a `for` loop too early.
* Understanding why `return True` should only occur after all required resources have been checked.
* Processing multiple types of coins and converting their values into naira-independent decimal currency values.
* Calculating whether the customer's payment is sufficient.
* Understanding the difference between the customer's payment, the change returned, and the machine's revenue.
* Making sure only the price of the coffee is added to the machine's money.
* Updating the machine's resources after successfully making a coffee.
* Understanding how functions can simplify and organize a larger program.
* Keeping the coffee machine running until the user enters `off`.
* Handling special commands such as `report` and `off`.
* Using dictionary membership to validate coffee selections.
* Designing the program so that adding another coffee would require minimal changes to the main logic.
* Debugging and refactoring the program before comparing my implementation with the instructor's solution.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add stronger input validation for coffee selections.
* Prevent invalid or negative coin quantities.
* Handle non-numeric input when entering coins.
* Add a more robust currency and payment system.
* Improve the way change is calculated and returned.
* Add more coffee types and recipes.
* Add additional ingredients such as chocolate or syrup.
* Add different sizes such as small, medium, and large.
* Add a stock-replenishment feature for the machine.
* Add low-resource warnings before resources run out.
* Track the number of each type of coffee sold.
* Display sales statistics in the report.
* Add a daily sales or revenue report.
* Add an option for the machine operator to restock resources.
* Improve the user interface and terminal presentation.
* Create a graphical user interface.
* Separate the coffee machine logic from the user interface even further.
* Store machine settings and sales data in a file or database.
* Add automated tests for functions such as `check_resources_sufficient()`, `process_coins()`, and `check_transaction_successful()`.
