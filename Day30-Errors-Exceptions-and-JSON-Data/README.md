# Day 30 – Errors, Exceptions & JSON Data

## Topics Covered

* Error handling
* Exceptions
* `try`
* `except`
* `else`
* `finally`
* `FileNotFoundError`
* Handling errors without crashing the program
* Reading files with `open()`
* Writing files with `open()`
* Reading JSON data
* Writing JSON data
* The `json` module
* `json.load()`
* `json.dump()`
* Dictionaries
* Nested dictionaries
* Dictionary keys and values
* Checking whether a key exists using `in`
* Updating dictionaries with `.update()`
* Accessing values from nested dictionaries
* List comprehensions
* Functions
* Function parameters and arguments
* User input through Tkinter `Entry` widgets
* `messagebox`
* Exception handling in GUI applications
* Persistent data storage
* Generating random passwords
* Copying text to the clipboard with `pyperclip`
* Building a password manager
* Combining GUI programming with file storage
* Separating program functionality into functions

## Project

### Password Manager

A graphical password manager built with Tkinter.

The application allows the user to:

* Enter a website
* Enter an email or username
* Generate a random password
* Copy the generated password to the clipboard
* Save website credentials to a JSON file
* Search for previously saved credentials
* Display saved login details through a message box

The project builds on the Password Manager created in earlier days and introduces **JSON data storage and exception handling**.

Instead of keeping password information only in memory while the program is running, the application stores the data in a `data.json` file so that it can be retrieved later.

## How It Works

The program:

1. Creates a Tkinter graphical user interface.
2. Allows the user to enter a website.
3. Allows the user to enter an email or username.
4. Generates a random password when requested.
5. Copies generated passwords to the clipboard.
6. Creates a nested dictionary containing the website credentials.
7. Checks whether required fields have been completed.
8. Attempts to open the JSON data file.
9. Handles `FileNotFoundError` if the data file does not exist.
10. Creates a new JSON file when necessary.
11. Loads existing JSON data using `json.load()`.
12. Updates the existing dictionary with new credentials.
13. Saves the updated dictionary using `json.dump()`.
14. Clears the website and password fields after saving.
15. Searches the JSON data for a requested website.
16. Displays the stored email and password if the website exists.
17. Displays an error message if no data file or website details are found.

## Error and Exception Handling

One of the main concepts introduced in Day 30 is handling exceptions.

Instead of allowing the program to crash when a file does not exist, the program can catch the exception:

```python
try:
    with open("./Day30/data.json", "r") as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    messagebox.showinfo(
        title="Error",
        message="No Data File Found."
    )
```

This allows the program to respond appropriately when something goes wrong.

### `try`

The code that might cause an exception is placed inside the `try` block.

```python
try:
    with open("./Day30/data.json", "r") as data_file:
        data = json.load(data_file)
```

### `except`

The `except` block handles a particular exception.

```python
except FileNotFoundError:
    ...
```

### `else`

The `else` block runs when the `try` block completes successfully without raising the specified exception.

```python
else:
    data.update(new_data)
```

### `finally`

The `finally` block runs regardless of whether an exception occurred.

In the project, it is used to clear the input fields:

```python
finally:
    website_entry.delete(0, END)
    password_entry.delete(0, END)
```

## Working with JSON

JSON provides a convenient way to store structured data in a file.

For example, the password manager stores data in a structure similar to:

```json
{
    "example.com": {
        "email": "user@example.com",
        "password": "ExamplePassword123!"
    }
}
```

The JSON structure represents a Python nested dictionary.

### Reading JSON Data

The `json.load()` function converts JSON data from a file into Python data:

```python
with open("./Day30/data.json", "r") as data_file:
    data = json.load(data_file)
```

### Writing JSON Data

The `json.dump()` function writes Python data to a JSON file:

```python
with open("./Day30/data.json", "w") as data_file:
    json.dump(data, data_file, indent=4)
```

The `indent=4` argument formats the JSON file so that it is easier for humans to read.

## Updating Existing Data

When a new password is saved, a nested dictionary is created:

```python
new_data = {
    website: {
        "email": email,
        "password": password
    }
}
```

If the JSON file already contains data, the new dictionary is added to the existing data using `.update()`:

```python
data.update(new_data)
```

This allows multiple websites and their credentials to be stored in the same JSON file.

## Searching for Passwords

The password manager can search the stored JSON data using the website entered by the user.

```python
if website in data:
    email = data[website]["email"]
    password = data[website]["password"]

    messagebox.showinfo(
        title=website,
        message=f"Email: {email}, \nPassword: {password}"
    )
```

The `in` operator checks whether the website exists as a key in the dictionary.

The nested dictionary is then accessed to retrieve the email and password.

## Code

### Password Generator

```python
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [
        choice(letters)
        for _ in range(randint(8, 10))
    ]

    password_symbols = [
        choice(symbols)
        for _ in range(randint(2, 4))
    ]

    password_numbers = [
        choice(numbers)
        for _ in range(randint(2, 4))
    ]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)
```

### Saving Password Data

```python
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty."
        )

    else:
        try:
            with open("./Day30/data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("./Day30/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("./Day30/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
```

### Finding Password Data

```python
def find_password():

    website = website_entry.get()

    try:
        with open("./Day30/data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Error",
            message="No Data File Found."
        )

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(
                title=website,
                message=f"Email: {email}, \nPassword: {password}"
            )

        else:
            messagebox.showinfo(
                title="Error",
                message="No details for website exists."
            )
```

## My Implementation

My implementation of the password search used a dictionary comprehension:

```python
result = {
    email: password
    for (email, password) in data[website].items()
}
```

I then accessed the resulting dictionary:

```python
messagebox.showinfo(
    title=website,
    message=f"Email: {result['email']}, \nPassword: {result['password']}"
)
```

Angela Yu's implementation accessed the nested dictionary directly:

```python
email = data[website]["email"]
password = data[website]["password"]
```

Both approaches can retrieve the stored values, but the direct approach is simpler for this particular data structure.

This was useful practice in understanding that the same problem can sometimes be solved using different Python techniques.

## What I Learned

* How exceptions occur when Python encounters an error during program execution.
* How to use `try` to test code that may raise an exception.
* How to use `except` to handle specific exceptions.
* How to handle `FileNotFoundError`.
* How to use `else` when code should run only if no exception occurred.
* How to use `finally` for code that should run regardless of whether an exception occurred.
* How exception handling can prevent a program from crashing.
* How to use the `json` module.
* How to read JSON data using `json.load()`.
* How to write JSON data using `json.dump()`.
* How Python dictionaries can be stored as JSON.
* How to work with nested dictionaries.
* How to update an existing dictionary using `.update()`.
* How to check whether a dictionary contains a particular key using `in`.
* How to access values inside nested dictionaries.
* How to create structured data before saving it to a file.
* How to create a JSON file when one does not already exist.
* How to load existing data before adding new information.
* How to persist program data between executions.
* How to combine JSON file storage with a Tkinter GUI.
* How to use `messagebox` to display information and errors.
* How to use dictionary comprehensions.
* How to use `.items()` to iterate through dictionary key-value pairs.
* How to generate random passwords using `choice()`, `randint()`, and `shuffle()`.
* How to copy generated passwords to the clipboard using `pyperclip`.
* How to build a more complete password manager application.
* How to organize different parts of a larger application into separate functions.
* How error handling can make a program more robust.
* How persistent storage allows information to remain available after a program closes.

## Challenges

* Understanding what an exception is and why it occurs.
* Understanding the purpose of `try` and `except`.
* Understanding how `FileNotFoundError` occurs when attempting to open a file that does not exist.
* Understanding how to create a new JSON file when the original data file is missing.
* Understanding the difference between `json.load()` and `json.dump()`.
* Understanding how JSON data corresponds to Python dictionaries.
* Working with nested dictionaries.
* Accessing values several levels deep inside a dictionary.
* Updating existing JSON data without overwriting previously stored information.
* Understanding how `.update()` combines new dictionary data with existing data.
* Checking whether a website exists in the stored data.
* Understanding the purpose of `else` in exception handling.
* Understanding the purpose of `finally`.
* Understanding how `finally` can be used for cleanup operations.
* Deciding how to retrieve values from a nested dictionary.
* Understanding the difference between direct dictionary access and a dictionary comprehension.
* Combining file operations, JSON, dictionaries, exception handling, and Tkinter.
* Debugging file paths and JSON files.
* Understanding how persistent data differs from variables that exist only while the program is running.
* Comparing my own implementation with Angela Yu's solution and understanding different approaches to solving the same problem.

## Future Improvements

* Encrypt stored passwords instead of storing them as plain text.
* Add stronger password-generation options.
* Allow the user to select password length.
* Allow the user to customize the number of letters, numbers, and symbols.
* Add username/email validation.
* Add stronger website validation.
* Add confirmation before overwriting existing credentials.
* Add the ability to edit existing credentials.
* Add the ability to delete credentials.
* Add a "Show Password" option.
* Add password-strength indicators.
* Add password search/autocomplete.
* Add categories for stored credentials.
* Add timestamps for saved credentials.
* Add automatic backup of the JSON data.
* Add better error handling for corrupted JSON files.
* Handle invalid JSON data using `json.JSONDecodeError`.
* Encrypt the data file or use a secure password-storage system.
* Separate the user interface from the password-management logic.
* Add automated tests.
* Improve the graphical user interface.
* Add a master password.
* Replace plain JSON storage with a database for a larger application.
* Add secure authentication and access control.
* Package the application as a standalone desktop application.

## Key Takeaway

Day 30 brought together several concepts learned throughout the previous days:

**Tkinter + Functions + Dictionaries + File Handling + JSON + Exceptions + Randomization**

The result is a program that can not only perform operations while it is running, but can also **store and retrieve information between program executions while handling situations where files or data may not exist**.