import requests
from datetime import datetime
import time
import os
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_PATH = os.path.join(SCRIPT_DIR, 'token.json')
CREDENTIALS_PATH = os.path.join(SCRIPT_DIR, 'credentials.json')


SCOPES = ['https://www.googleapis.com/auth/gmail.send']

MY_LAT = 8.997438
MY_LONG = 7.372418


def get_gmail_service():
    creds = None
    
    # Check if token.json exists (saved from previous login)
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    # If no valid credentials, ask user to log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next run
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    
    return build('gmail', 'v1', credentials=creds)

def send_email():
    service = get_gmail_service()
    
    message = MIMEText("Henry look up!")
    message['to'] = "chineduhenry05@yahoo.com"
    message['from'] = "henrypython648@gmail.com"
    message['subject'] = "Look Up"
    
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    
    try:
        service.users().messages().send(userId="me", body={'raw': raw}).execute()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    if is_iss_overhead() and is_night():
        send_email()
    time.sleep(60)


    
