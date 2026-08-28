# Day 17 – Quiz Game (Object-Oriented Programming)

## Topics Covered

* Object-Oriented Programming (OOP)
* Classes
* Objects
* Creating objects from classes
* Constructors with `__init__()`
* The `self` parameter
* Instance attributes
* Instance methods
* Creating custom classes
* Importing classes from another Python file
* Lists
* Lists of objects
* Dictionaries
* Accessing dictionary values using keys
* Iterating through lists
* `for` loops
* `while` loops
* Conditional statements (`if`, `elif`, `else`)
* Boolean values
* Comparison operators
* User input with `input()`
* String formatting with f-strings
* Returning values from methods
* Tracking program state
* Updating variables during program execution
* Building reusable classes and methods
* Separating data, models, and program logic into different files
* Building an interactive command-line program

## Project

### Quiz Game

A command-line quiz game that presents the player with a series of questions and allows them to answer each question.

The questions and answers are stored as structured data. Each question is converted into a `Question` object and stored in a question bank.

The program then presents the questions one at a time, checks the player's answers, keeps track of the score, and displays the final result when the quiz is complete.

This project introduces Object-Oriented Programming by using a custom `Question` class to represent individual quiz questions.

## How It Works

The program:

1. Imports the quiz question data.
2. Imports the `Question` class from a separate module.
3. Creates an empty question bank.
4. Loops through the question data.
5. Extracts the question text and answer from each dictionary.
6. Creates a `Question` object for each question.
7. Adds each `Question` object to the question bank.
8. Uses the question bank to run the quiz.
9. Displays each question to the player.
10. Gets the player's answer using `input()`.
11. Checks the player's answer against the correct answer.
12. Updates the player's score when an answer is correct.
13. Continues until all questions have been answered.
14. Displays the player's final score.

## Object-Oriented Structure

The project uses a custom class to represent quiz questions.

### `Question`

The `Question` class represents an individual quiz question.

Each `Question` object stores information such as:

- The question text
- The correct answer

For example:

```python
class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
````

A question object can then be created from the data:

```python
new_question = Question(
    question["text"],
    question["answer"]
)
```

## Creating the Question Bank

The question data is stored as a list containing dictionaries.

Each dictionary contains the question text and its answer.

The dictionaries are converted into `Question` objects and stored in a separate list:

```python
question_bank = []

for question in question_data:
    new_question = Question(
        question["text"],
        question["answer"]
    )
    question_bank.append(new_question)
```

This allows the program to work with `Question` objects rather than repeatedly accessing dictionary keys throughout the quiz.

## Code

### `Question` Class

```python
class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
```

### Building the Question Bank

```python
question_bank = []

for question in question_data:
    new_question = Question(
        question["text"],
        question["answer"]
    )
    question_bank.append(new_question)
```

The question bank is therefore a list of `Question` objects that can be accessed throughout the quiz.

## What I Learned

* How to create a custom class using the `class` keyword.
* How to create objects from a custom class.
* How to use `__init__()` to initialize an object.
* How the `self` parameter refers to the current object.
* How to create instance attributes such as `text` and `answer`.
* How to store related information inside objects.
* How to import a custom class from another Python file.
* How to use a list containing dictionaries as a source of structured data.
* How to access dictionary values using keys.
* How to convert dictionaries into objects.
* How to create a list of objects.
* How to use `for` loops to process a collection of questions.
* How to use `while` loops to control the quiz.
* How to use conditional statements to determine whether an answer is correct.
* How to use Boolean values to control program logic.
* How to use user input to interact with the quiz.
* How to compare the user's answer with the correct answer.
* How to keep track of the player's score.
* How to update variables as the quiz progresses.
* How to use object attributes to access information stored in an object.
* How to use methods to give objects behavior.
* How to separate data, object definitions, and program logic into different modules.
* How Object-Oriented Programming can make a program more organized and easier to expand.
* How to convert structured data into objects that can be used throughout a program.
* How to build a complete interactive program using classes, objects, lists, loops, and user input.

## Challenges

* Understanding the difference between a class and an object.
* Understanding how the `Question` class represents an individual question.
* Understanding how `__init__()` initializes a new object.
* Understanding the purpose of the `self` parameter.
* Understanding how instance attributes store information belonging to an object.
* Understanding how to import a custom class from another Python file.
* Understanding the structure of the `question_data` list.
* Accessing dictionary values using keys such as `"text"` and `"answer"`.
* Understanding how a dictionary can be converted into a `Question` object.
* Understanding the difference between storing a dictionary and storing an object.
* Building a question bank containing multiple `Question` objects.
* Understanding how to access attributes from objects stored in a list.
* Managing the flow of the quiz using loops.
* Keeping track of the current question while the quiz progresses.
* Keeping track of the player's score.
* Comparing the user's answer with the correct answer.
* Understanding how different parts of the program communicate through objects and methods.
* Separating the question model from the main quiz logic.
* Understanding how Object-Oriented Programming can simplify a larger program.
* Comparing my own implementation with the instructor's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Add stronger input validation for quiz answers.
* Accept different variations of correct answers.
* Make answer comparison case-insensitive.
* Randomize the order of the questions.
* Add different categories of questions.
* Add multiple-choice questions.
* Add more than two possible answers.
* Add difficulty levels.
* Add a timer for each question.
* Add a limited number of lives.
* Track the player's highest score.
* Save quiz scores to a file or database.
* Add a leaderboard.
* Allow the player to choose the number of questions.
* Add a "Play Again?" option.
* Display the percentage of questions answered correctly.
* Add progress information such as `Question 5 of 20`.
* Improve the terminal user interface.
* Add colored terminal output.
* Add sound effects or animations.
* Create a graphical user interface.
* Separate the quiz engine from the user interface even further.
* Add automated tests for the `Question` class and quiz logic.
* Expand the project into a reusable quiz framework that can support different question sets and subjects.
