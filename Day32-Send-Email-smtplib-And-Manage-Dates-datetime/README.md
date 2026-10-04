# Day 32 – Birthday Wisher with Gmail API & GitHub Actions

## Topics Covered

* Python
* Reading CSV data with Pandas
* DataFrame iteration with `.iterrows()`
* Dictionary comprehensions
* Tuples as dictionary keys
* Date handling with `datetime`
* Comparing dates using tuples
* Working with external data files
* File reading and writing
* String replacement with `.replace()`
* Random selection with `random.randint()`
* Sending email via the Gmail API
* Google OAuth 2.0 authentication
* Managing credentials with `credentials.json` and `token.json`
* Scopes and permissions
* Base64 encoding for email messages
* MIME message construction with `MIMEText`
* Environment variables with `os.getenv()`
* Robust file paths with `pathlib.Path`
* Using `Path(__file__).parent` for script-relative paths
* Separating configuration from code
* Guarding script execution with `if __name__ == "__main__"`
* Refactoring a script into reusable functions
* Scheduling scripts with GitHub Actions
* Writing YAML workflow files
* Cron expressions for scheduled workflows
* Using GitHub Actions secrets for sensitive data
* Recreating local files on a CI runner from secrets
* Automating a Python script in the cloud

## Project

### Birthday Wisher

An automated birthday reminder and email sender that checks a CSV file of birthdays and sends a personalized birthday letter to anyone whose birthday matches today's date.

The application reads birthdays from a CSV file, builds a lookup dictionary keyed by `(month, day)` tuples, and checks whether today's date matches any entry. When it finds a match, it selects a random letter template, personalizes it with the celebrant's name, and sends it via email using the Gmail API.

Originally, Angela Yu's version of this project used SMTP with a Gmail app password. This version modernizes the email sending by using the **Gmail API with OAuth 2.0**, which is more secure and future-proof as Google continues to phase out less-secure authentication methods.

The project also demonstrates **cloud automation**: the script is scheduled to run automatically every morning using **GitHub Actions**, so no local machine needs to be running for the birthday email to be sent.

## How It Works

The program:

1. Gets today's date as a `(month, day)` tuple using `datetime.now()`.
2. Loads the birthdays data from `birthdays.csv` using Pandas.
3. Builds a dictionary where each key is a `(month, day)` tuple and each value is the corresponding row.
4. Checks whether today's date tuple exists as a key in the dictionary.
5. If a match is found:
   1. Retrieves the celebrant's row.
   2. Picks one of three letter templates at random.
   3. Reads the template and replaces `[NAME]` with the celebrant's name.
   4. Authenticates with the Gmail API (reusing saved credentials if possible).
   5. Constructs a MIME email message.
   6. Sends the email.
6. If no match is found, prints a friendly message and exits.

When scheduled on GitHub Actions, the process runs automatically each morning without any user intervention.

## Email Sending

The application uses the **Gmail API** to send emails.

Unlike SMTP with app passwords, the Gmail API uses OAuth 2.0, which requires a one-time user authorization to grant the script permission to send emails on the user's behalf.

The scope used is:

```python
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
```

This grants permission to send emails only — not to read, delete, or manage the inbox — following the principle of least privilege.

## Authentication Flow

The script handles authentication in `get_gmail_service()`:

1. **First run (local):** Opens a browser window and asks the user to log into their Google account and grant permission. The resulting credentials are saved to `token.json` so the user doesn't have to re-authenticate every time.
2. **Subsequent runs:** Loads `token.json` directly, refreshing it if expired.
3. **On GitHub Actions:** Both `credentials.json` and `token.json` are recreated from GitHub secrets before the script runs (see *Cloud Scheduling with GitHub Actions* below).

## Working with CSV Data

The birthday data is stored in a CSV file with the following columns:

```csv
name,email,year,month,day
Henry,chineduhenry05@yahoo.com,1961,10,3
```

The CSV file is loaded with Pandas:

```python
data = pd.read_csv(BIRTHDAYS_CSV)
```

Each row becomes an entry in the DataFrame, and each column is accessible by name.

## Building the Birthday Lookup Dictionary

A dictionary comprehension converts the DataFrame into a lookup table keyed by date:

```python
birthday_dict = {
    (row['month'], row['day']): row
    for (_, row) in data.iterrows()
}
```

- `.iterrows()` yields `(index, row)` pairs.
- `(row['month'], row['day'])` creates a tuple used as the key.
- The entire row is the value, so all the person's data stays accessible.

Tuples work as dictionary keys because they are immutable — this is what makes the `(month, day)` lookup pattern work.

## Date Matching

Today's date is stored as a tuple so it can be compared directly with dictionary keys:

```python
today = (datetime.now().month, datetime.now().day)
if today in birthday_dict:
    celebrant = birthday_dict[today]
```

This is an O(1) dictionary lookup — much faster and clearer than scanning the DataFrame.

## Personalizing the Letter

Three letter templates are stored in `letter_templates/`. One is selected at random:

```python
letter_path = LETTERS_DIR / f"letter_{randint(1, 3)}.txt"
```

The template contains a `[NAME]` placeholder that is replaced with the celebrant's name:

```python
with open(letter_path) as letter_file:
    message = letter_file.read().replace("[NAME]", celebrant['name'])
```

## Sending the Email

A MIME message is constructed and encoded:

```python
message = MIMEText(birthday_message)
message['to'] = email
message['from'] = SENDER_EMAIL
message['subject'] = "Happy Birthday!"

raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
```

The Gmail API expects the raw message to be Base64-encoded, which is why `base64.urlsafe_b64encode` is used.

The email is then sent:

```python
service.users().messages().send(userId="me", body={'raw': raw}).execute()
```

## Robust File Paths

Instead of hardcoding paths like `./Day32/birthdays.csv`, this version uses `pathlib.Path` anchored to the script's own location:

```python
BASE_DIR = Path(__file__).parent
TOKEN_PATH = BASE_DIR / "token.json"
CREDENTIALS_PATH = BASE_DIR / "credentials.json"
BIRTHDAYS_CSV = BASE_DIR / "birthdays.csv"
LETTERS_DIR = BASE_DIR / "letter_templates"
```

This makes the script work correctly regardless of the working directory it is run from — whether run locally, from the repo root, or on a GitHub Actions runner.

## Configuration with Environment Variables

The sender email address is read from an environment variable with a fallback:

```python
SENDER_EMAIL = os.getenv("MY_EMAIL", "henrypython648@gmail.com")
```

This allows the same code to run in different environments (local, CI) without modification, and keeps configuration out of source code.

## Cloud Scheduling with GitHub Actions

The script is scheduled to run automatically every day at 06:00 UTC using GitHub Actions.

The workflow file is located at `.github/workflows/birthday-wisher.yml` and:

1. Runs on a schedule (daily at 06:00 UTC).
2. Can also be triggered manually via `workflow_dispatch`.
3. Checks out the repository.
4. Sets up Python 3.11.
5. Installs required packages.
6. Recreates `credentials.json` and `token.json` from GitHub secrets.
7. Runs `main.py`.

Since the secrets are not stored in the repository, they must be recreated on the runner at runtime. This is done with:

```yaml
- name: Write credentials.json from secret
  working-directory: ./Day32-Send-Email-smtplib-And-Manage-Dates-datetime
  run: echo '${{ secrets.GMAIL_CREDENTIALS }}' > credentials.json
```

## Cron Syntax

The workflow uses a cron expression to define the schedule:

```
┌───────── minute (0–59)
│ ┌─────── hour (0–23 UTC)
│ │ ┌───── day of month
│ │ │ ┌─── month
│ │ │ │ ┌─ day of week
0 6 * * *
```

`0 6 * * *` means "at 06:00 UTC every day", which corresponds to approximately 07:00 in Nigeria (WAT, UTC+1).

## Code Structure

The project is organized into several functions with distinct responsibilities.

### `get_gmail_service()`

Responsible for:

* Checking for an existing `token.json`.
* Refreshing expired credentials.
* Running the OAuth flow if no valid credentials exist.
* Saving newly obtained credentials.
* Returning a Gmail API service object.

### `send_email(birthday_message, email)`

Responsible for:

* Constructing the MIME message.
* Setting the recipient, sender, and subject.
* Base64-encoding the raw message.
* Sending the message via the Gmail API.
* Handling exceptions.

### `main()`

Responsible for:

* Determining today's date.
* Loading the birthdays CSV.
* Building the lookup dictionary.
* Checking whether today matches any birthday.
* Reading and personalizing the letter template.
* Calling `send_email()` with the prepared message.

### `if __name__ == "__main__":`

Guards the script so that `main()` only runs when the file is executed directly, not when it is imported as a module.

## What I Learned

* How to read CSV data with Pandas and convert it into a dictionary.
* How to build dictionary lookups using tuples as keys.
* How to iterate over a DataFrame with `.iterrows()`.
* How to work with dates using `datetime`.
* How to send emails using the Gmail API instead of SMTP.
* How OAuth 2.0 authorization works at a high level.
* How to save and reuse OAuth credentials with `token.json`.
* How to construct MIME messages for email.
* How to Base64-encode raw email content.
* How to use environment variables for configuration.
* How to make file paths robust with `pathlib.Path` and `Path(__file__).parent`.
* Why separating credentials from code matters.
* How to refactor a script into clean, testable functions.
* How to use `if __name__ == "__main__":` correctly.
* How to write a GitHub Actions workflow in YAML.
* How to define a cron schedule for automated runs.
* How to store and use GitHub Actions secrets.
* How to recreate local configuration files on a CI runner.
* How to automate a Python script in the cloud for free.
* How to debug workflows by reading GitHub Actions logs.

## Challenges

* Setting up the Gmail API and OAuth credentials in Google Cloud Console.
* Understanding the difference between SMTP with app passwords and the Gmail API with OAuth.
* Managing `credentials.json` and `token.json` safely — making sure they never end up in the repository.
* Understanding how OAuth token refresh works and when it fails.
* Getting the scope right so the script can send but not read emails.
* Figuring out why the original script's hardcoded `./Day32/...` paths broke when run from GitHub Actions.
* Refactoring the code to use `Path(__file__).parent` so paths are independent of working directory.
* Learning YAML syntax and its strict indentation rules.
* Writing a cron expression that triggers at the correct local time.
* Understanding how GitHub Actions recreates secret files on the runner.
* Debugging the first workflow run when something went wrong in a step.
* Making sure the secrets were named exactly as referenced in the workflow.
* Understanding why `workflow_dispatch` is useful for testing.
* Handling the case where nobody has a birthday today gracefully, so the workflow exits cleanly.

## Future Improvements

* Add support for multiple recipients per birthday.
* Add a preview mode that sends the email to the developer only.
* Let the user edit letter templates without touching the source.
* Support HTML-formatted emails instead of plain text.
* Add attachments (e.g., a birthday card image).
* Support multiple senders or a rotation of senders.
* Add logging so every run is recorded with a timestamp.
* Send a notification if a send fails so the user is alerted.
* Add unit tests for the date-matching logic and dictionary building.
* Add support for sending not just on the exact day but also in advance.
* Support time zones other than UTC in the workflow schedule.
* Cache dependencies in the workflow for faster runs.
* Migrate secrets to an encrypted store for local runs too.
* Refactor the script into a package with modules.
* Add a CLI interface so the script can be run on demand locally.
* Store birthdays in a database instead of a CSV file.
* Add a simple web dashboard for managing birthdays.
* Support SMS or WhatsApp as additional notification channels.
* Add CI checks (linting, formatting) alongside the scheduled run.
* Add a badge to the README showing the last workflow run status.

## Project Reflection

This project was a significant step forward from previous days because it combined three areas that were each new in different ways:

* **Cloud automation** — moving from "run it on my laptop" to "it runs itself every day on GitHub's servers".
* **Modern authentication** — replacing the deprecated SMTP + app password approach with the OAuth 2.0-based Gmail API.
* **Robust code organization** — using `pathlib` for portable paths, environment variables for configuration, and proper function separation.

It also introduced an important concept for real-world software: **configuration and secrets should not live in code**. Handling this correctly meant learning about GitHub Actions secrets, writing files at runtime on a runner, and verifying that nothing sensitive was ever committed.

The project demonstrated that automation isn't just about writing a script that works once — it's about making it work reliably, securely, and repeatedly without human intervention. Moving from a locally-run script to a cloud-scheduled one made the difference between a learning exercise and a genuinely useful tool.

Finally, the debugging process — verifying YAML indentation, checking that secrets were named exactly, and confirming file paths worked from the runner's working directory — reinforced how important it is to test and observe the behavior of code in the actual environment it will run in.
