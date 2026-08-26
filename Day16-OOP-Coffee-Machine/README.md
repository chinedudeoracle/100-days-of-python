# Day 16 – Coffee Machine (Object-Oriented Programming)

## Topics Covered

* Object-Oriented Programming (OOP)
* Classes
* Objects
* Creating objects from classes
* Attributes
* Methods
* Constructors with `__init__()`
* The `self` parameter
* Instance attributes
* Instance methods
* Class-based program organization
* Encapsulation
* Importing classes from modules
* Using objects from external Python files
* Dictionaries inside classes
* Lists of objects
* Accessing object attributes
* Calling object methods
* Returning values from methods
* Conditional statements (`if`, `elif`, `else`)
* `for` loops
* `while` loops
* Boolean values
* Comparison operators
* User input with `input()`
* String methods such as `.lower()` and `.strip()`
* Managing program state with objects
* Separating data and behavior
* Refactoring a procedural program into an object-oriented program
* Building a larger command-line program using multiple classes

## Project

### Coffee Machine – Object-Oriented Version

An object-oriented command-line coffee machine program that allows users to purchase different types of coffee.

The project builds on the Coffee Machine from Day 15, but instead of managing all of the machine's data and functionality using dictionaries and standalone functions, the program uses classes and objects.

The coffee machine is divided into separate components, with each class responsible for a specific part of the system.

The main components include:

- `MenuItem` – Represents an individual coffee item and its ingredients and cost.
- `Menu` – Stores the available menu items and provides methods for finding drinks.
- `CoffeeMaker` – Manages the machine's resources and prepares coffee.
- `MoneyMachine` – Handles payment, coins, transactions, and the machine's money.

This project demonstrates how Object-Oriented Programming can be used to organize a larger Python program into smaller, reusable components.

## How It Works

The program:

1. Creates objects representing the coffee menu, coffee maker, and money machine.
2. Displays the available coffee options.
3. Asks the user which coffee they would like.
4. Allows the user to enter `report` to view the machine's resources and money.
5. Allows the user to enter `off` to shut down the machine.
6. Searches the menu for the requested coffee.
7. Checks whether the coffee machine has enough resources.
8. Processes the user's payment.
9. Checks whether the payment is sufficient.
10. Calculates and returns change when necessary.
11. Deducts the required ingredients from the machine's resources.
12. Adds the coffee price to the machine's money.
13. Dispenses the selected coffee.
14. Continues running until the user enters `off`.

Each major responsibility is handled by a different class rather than being controlled entirely by one large function.

## Object-Oriented Structure

The project uses several classes to organize the coffee machine.

### `MenuItem`

Represents an individual drink.

It stores information such as:

- Drink name
- Required water
- Required milk
- Required coffee
- Cost

### `Menu`

Manages the available drinks.

It can:

- Store menu items
- Display available drinks
- Search for a particular drink

### `CoffeeMaker`

Manages the coffee machine itself.

It is responsible for:

- Storing available resources
- Reporting resources
- Checking whether resources are sufficient
- Making coffee
- Deducting ingredients after a successful purchase

### `MoneyMachine`

Manages the financial side of the machine.

It is responsible for:

- Accepting coins
- Calculating the inserted amount
- Checking whether payment is sufficient
- Returning change
- Tracking the machine's money

## Code

```python
class MenuItem:
    """Models each item on the coffee machine menu."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost

        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """Models the coffee machine menu."""

    def __init__(self):
        self.menu = [
            MenuItem(
                name="espresso",
                water=50,
                milk=0,
                coffee=18,
                cost=1.5,
            ),
            MenuItem(
                name="latte",
                water=200,
                milk=150,
                coffee=24,
                cost=2.5,
            ),
            MenuItem(
                name="cappuccino",
                water=250,
                milk=100,
                coffee=24,
                cost=3.0,
            ),
        ]

    def get_items(self):
        """Returns the names of the available menu items."""
        options = ""

        for item in self.menu:
            options += f"{item.name}/"

        return options

    def find_drink(self, order_name):
        """Searches the menu for a drink with the given name."""

        for item in self.menu:
            if item.name == order_name:
                return item

        return None
````

## What I Learned

* How Object-Oriented Programming can be used to structure a Python program.
* How to define classes using the `class` keyword.
* How to create objects from classes.
* How to define a constructor using `__init__()`.
* How the `self` parameter refers to the current object.
* How to create and access instance attributes.
* How to define methods that belong to a class.
* How to call methods using objects.
* How to store related data and behavior inside a class.
* How to use objects to represent real-world components of a program.
* How to create multiple objects from the same class.
* How to use lists to store multiple objects.
* How to access attributes belonging to objects stored in a list.
* How to use dictionaries inside classes to store related data.
* How to return values from methods.
* How to use `None` when a method does not find a matching object.
* How to import classes from other Python files.
* How to divide a larger program into multiple modules.
* How to give different classes separate responsibilities.
* How Object-Oriented Programming can improve code organization.
* How to refactor a procedural program into an object-oriented program.
* How the same coffee machine functionality from Day 15 can be organized using classes and objects.
* How encapsulating related data and functionality can make a program easier to understand and maintain.

## Challenges

* Understanding the difference between a class and an object.
* Understanding when to create a class instead of using a normal function.
* Understanding how `__init__()` works when an object is created.
* Understanding the purpose of the `self` parameter.
* Understanding the difference between instance attributes and local variables.
* Understanding how methods can access attributes belonging to the same object.
* Understanding how multiple objects can be created from the same class.
* Understanding how objects can be stored inside lists.
* Accessing attributes from objects stored inside a list.
* Understanding how the different classes work together.
* Understanding why each class should have a specific responsibility.
* Understanding how the `Menu` class can manage `MenuItem` objects.
* Understanding how the `CoffeeMaker` class manages resources and makes coffee.
* Understanding how the `MoneyMachine` class handles payments and money.
* Understanding how importing classes from separate files helps organize a larger project.
* Refactoring the procedural Coffee Machine from Day 15 into an object-oriented design.
* Understanding how methods can replace some of the standalone functions used in the previous version.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add stronger input validation for coffee selections.
* Prevent invalid or negative coin quantities.
* Handle non-numeric input when entering coins.
* Add more coffee types and recipes.
* Add additional ingredients such as chocolate or syrup.
* Add different drink sizes such as small, medium, and large.
* Add a stock-replenishment system.
* Add low-resource warnings.
* Track the number of each type of coffee sold.
* Add sales statistics to the machine's report.
* Add a daily sales or revenue report.
* Add an operator mode for managing the machine.
* Allow the machine's menu to be modified while the program is running.
* Store machine settings and sales data in a file or database.
* Add automated tests for the different classes and methods.
* Create a graphical user interface.
* Separate the user interface from the business logic even further.
* Add logging for transactions and machine events.
* Expand the project into a more realistic coffee-shop management system.
