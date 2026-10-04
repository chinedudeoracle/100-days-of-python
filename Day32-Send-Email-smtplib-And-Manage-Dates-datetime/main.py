from pathlib import Path
from datetime import datetime
from random import randint
import os
import base64

import pandas as pd
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail API scope (send-only)
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# All file paths are anchored to the folder where this script lives.
# This makes the script work regardless of the current working directory,
# whether run locally, from the repo root, or on a GitHub Actions runner.
BASE_DIR         = Path(__file__).parent
TOKEN_PATH       = BASE_DIR / "token.json"
CREDENTIALS_PATH = BASE_DIR / "credentials.json"
BIRTHDAYS_CSV    = BASE_DIR / "birthdays.csv"
LETTERS_DIR      = BASE_DIR / "letter_templates"

# Read sender address from env var (set in GitHub Actions), fall back to hardcoded.
SENDER_EMAIL = os.getenv("MY_EMAIL", "henrypython648@gmail.com")


def get_gmail_service():
    """Authenticate with Gmail and return a service object."""
    creds = None

    # Reuse saved credentials if they exist
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    # If no valid creds, either refresh or run the OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_PATH), SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save for next time
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


def send_email(birthday_message, email):
    """Send the birthday message via the Gmail API."""
    service = get_gmail_service()

    message = MIMEText(birthday_message)
    message['to'] = email
    message['from'] = SENDER_EMAIL
    message['subject'] = "Happy Birthday!"

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        service.users().messages().send(
            userId="me", body={'raw': raw}
        ).execute()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def main():
    today = (datetime.now().month, datetime.now().day)

    data = pd.read_csv(BIRTHDAYS_CSV)
    birthday_dict = {
        (row['month'], row['day']): row
        for (_, row) in data.iterrows()
    }

    if today in birthday_dict:
        celebrant = birthday_dict[today]
        letter_path = LETTERS_DIR / f"letter_{randint(1, 3)}.txt"

        with open(letter_path, "r") as letter_file:
            message = letter_file.read().replace("[NAME]", celebrant['name'])

        send_email(birthday_message=message, email=celebrant['email'])
    else:
        print(f"No birthdays today ({today[0]}/{today[1]}).")


if __name__ == "__main__":
    main()