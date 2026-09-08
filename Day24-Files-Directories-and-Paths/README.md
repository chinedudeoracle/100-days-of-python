# Day 24 – Files, Directories and Paths

## Topics Covered

- File handling in Python
- Reading files using `open()`
- Reading the entire content of a file
- Reading a file line by line
- Writing to files using `write()`
- Appending to files using `"a"` mode
- Working with file paths
- Absolute vs relative paths
- Using `os` and `pathlib` modules
- The `with` statement (context managers)
- Automatically closing files
- Error handling with file operations
- Reading from and writing to `.txt` files
- String manipulation and replacement
- Using `replace()` to modify text content
- Working with directories
- Creating directories
- Checking if a file or directory exists
- The `os.path` module
- Using `os.getcwd()` to get the current working directory
- Changing directories with `os.chdir()`
- Building paths using `os.path.join()`
- Understanding the `__file__` variable
- Working with relative paths from the current script
- The `pathlib.Path` class
- Using `Path().resolve()` to get absolute paths
- Reading and writing files from different directories
- The Mail Merge project workflow
- Using a list of names to generate personalized files
- Combining file reading, string manipulation, and file writing

## Project

### Mail Merge

A practical project that automates the process of generating personalized invitation letters.

The program reads a list of names from a file and a template letter, then creates a separate personalized letter for each person.

The program:

1. Reads a list of names from a text file.
2. Reads a template letter containing placeholder text.
3. Replaces the placeholder with each person's name.
4. Creates a new text file for each person containing their personalized letter.

This demonstrates how file handling can be used to automate repetitive document creation tasks.

## How It Works

The program:

1. Opens the names file (`invited_names.txt`) and reads all the names.
2. Stores the names in a list.
3. Opens the template letter (`starting_letter.txt`) and reads its content.
4. For each name in the names list:
   - Replaces the placeholder `[name]` with the person's actual name.
   - Creates a new file in the `Output/ReadyToSend` directory.
   - Writes the personalized letter content to the new file.
5. Closes all files automatically using the `with` statement.
6. Creates the output directory if it does not already exist.

## File Structure

The project uses the following file structure:

```
Mail Merge Project/
│
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   └── Letters/
│       └── starting_letter.txt
│
└── Output/
    └── ReadyToSend/
        ├── letter_for_Angela.txt
        ├── letter_for_Ben.txt
        └── ...
```

The `Input` folder contains the source files, and the `Output/ReadyToSend` folder contains the generated personalized letters.

## File Operations

### Reading a File

```python
with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()
```

The `with` statement automatically closes the file after the block finishes executing.

### Reading a Template

```python
with open("Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()
```

### Writing Personalized Letters

```python
for name in names:
    personalized_letter = letter_template.replace("[name]", name)
    
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(personalized_letter)
```

## Working with Paths

### Getting the Current Working Directory

```python
import os

current_path = os.getcwd()
print(current_path)
```

### Building Paths Across Operating Systems

```python
import os

file_path = os.path.join("Input", "Names", "invited_names.txt")
```

### Using `pathlib` (Modern Approach)

```python
from pathlib import Path

file_path = Path("Input") / "Names" / "invited_names.txt"
```

### Relative Paths Using `__file__`

```python
from pathlib import Path

script_location = Path(__file__).resolve()
project_root = script_location.parent
```

This allows the program to work correctly regardless of where the script is executed from.

## The `with` Statement (Context Managers)

The `with` statement ensures that files are properly closed, even if an exception occurs.

**Without `with` (Manual):**

```python
file = open("example.txt", "r")
content = file.read()
file.close()
```

**With `with` (Automatic):**

```python
with open("example.txt", "r") as file:
    content = file.read()
```

Using `with` is considered a best practice because it prevents resource leaks.

## String Replacement

The `replace()` method is used to substitute placeholders with actual values.

```python
new_text = original_text.replace("[name]", "Angela")
```

This allows the same template to be reused for different names.

## Code

### Main Program

```python
from pathlib import Path

# Get the project directory
project_dir = Path(__file__).resolve().parent

# Build file paths
names_path = project_dir / "Input" / "Names" / "invited_names.txt"
template_path = project_dir / "Input" / "Letters" / "starting_letter.txt"
output_dir = project_dir / "Output" / "ReadyToSend"

# Create output directory if it doesn't exist
output_dir.mkdir(parents=True, exist_ok=True)

# Read names
with open(names_path) as file:
    names = file.read().splitlines()

# Read template
with open(template_path) as file:
    letter_template = file.read()

# Generate personalized letters
for name in names:
    personalized_letter = letter_template.replace("[name]", name)
    
    output_path = output_dir / f"letter_for_{name}.txt"
    
    with open(output_path, "w") as file:
        file.write(personalized_letter)

print("Mail merge complete! Personalized letters created.")
```

## What I Learned

- How to read and write files using Python.
- How to use the `open()` function with different modes (`"r"`, `"w"`, `"a"`).
- How the `with` statement simplifies file handling by automatically closing files.
- Why it is important to close files after reading or writing.
- How to work with file paths using `os` and `pathlib`.
- The difference between absolute and relative paths.
- How to build paths that work on different operating systems.
- How to use `os.getcwd()` to find the current working directory.
- How to use `os.path.join()` to build paths safely.
- How to use `pathlib.Path` to work with paths in an object-oriented way.
- How to use the `__file__` variable to get the current script's location.
- How to create directories using `mkdir()` and `mkdirs()`.
- How to check whether a file or directory exists.
- How to read lines from a file into a list using `splitlines()`.
- How to use the `replace()` method to substitute placeholders in text.
- How to generate multiple output files using a loop.
- How to organize files into input and output directories.
- How to automate a real-world document generation task.
- How file handling, string manipulation, and loops can work together to solve practical problems.
- How proper path management makes code more portable and reliable.
- How to build a program that is easy to run from any directory.

## Challenges

- Understanding the difference between absolute and relative paths.
- Understanding the current working directory and why it matters.
- Using `os.getcwd()` to determine where the script is running.
- Building paths that work on both Windows and macOS.
- Using `os.path.join()` instead of manually concatenating strings.
- Understanding why string concatenation with `+` can break on different systems.
- Understanding the `pathlib` module and its advantages over `os` and `os.path`.
- Converting between different path formats.
- Using `Path().resolve()` to get the absolute path of a relative path.
- Understanding the `__file__` variable and how it differs from the current working directory.
- Using `__file__` to make scripts more portable.
- Understanding why using a relative path like `"Input/Names/names.txt"` can fail when the script is run from a different directory.
- Using the `with` statement correctly with file operations.
- Understanding what happens if a file does not exist.
- Handling `FileNotFoundError` when opening a file.
- Creating directories with `mkdir()` and handling `FileExistsError`.
- Using `exist_ok=True` to avoid errors when a directory already exists.
- Using `replace()` to handle placeholder substitution.
- Ensuring that every placeholder in the template is correctly replaced.
- Generating multiple output files with unique names.
- Organizing the project into separate input and output directories.
- Understanding the complete Mail Merge workflow.
- Comparing my own implementation with the instructor's solution.
- Understanding how the same project can be implemented using `os` or `pathlib`.

## Future Improvements

- Add support for different placeholder formats.
- Add support for multiple placeholders (e.g., `[name]`, `[date]`, `[company]`).
- Add support for CSV files instead of text files.
- Add support for Word documents or PDF files.
- Add a graphical user interface.
- Add logging to track which files were created.
- Add error handling for missing files.
- Add validation for the template file format.
- Add the ability to choose different templates.
- Add preview functionality before generating files.
- Add the ability to send emails directly after generating the letters.
- Add support for formatting names (e.g., converting to title case).
- Add support for different output formats (e.g., `.docx`, `.pdf`).
- Add support for batch processing multiple templates.
- Add command-line arguments for input and output paths.
- Add unit tests for the file handling and replacement logic.
- Refactor the program into reusable functions.
- Create a class-based version of the mail merge program.
- Add performance improvements for processing large numbers of names.
- Add progress indicators for long-running operations.
- Add support for reading names from databases or APIs.

