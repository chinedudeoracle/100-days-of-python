# Day 33: API Endpoints & API Parameters — ISS Overhead Notifier

## Project Overview

A Python script that checks whether the International Space Station (ISS) is
currently overhead and whether it's dark outside. If both conditions are true,
it sends an email telling you to look up.

This project was built as part of **Day 33** of the
[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
by Dr. Angela Yu.

---

## How It Works

The script runs in an infinite loop, checking every 60 seconds:

1. **Fetches the current ISS position** from the
   [Open Notify ISS API](http://api.open-notify.org/iss-now.json).
2. **Fetches sunrise and sunset times** for your location from the
   [Sunrise-Sunset API](https://api.sunrise-sunset.org/json).
3. **Checks two conditions:**
   - Is the ISS within ±5° of your latitude and longitude?
   - Is it currently dark outside (before sunrise or after sunset)?
4. **If both are true**, it sends an email using the Gmail API.

---

## Concepts Practiced

- Working with **REST APIs** and `requests`
- Using **API parameters** (`params={...}`) to customize requests
- Parsing **JSON responses** into Python dictionaries
- Using **`response.raise_for_status()`** for error handling
- Working with **`datetime`** to compare hours of the day
- **Refactoring** logic into small, focused functions
- **OAuth 2.0 authentication** with the Gmail API
- Using **`time.sleep()`** to schedule repeated checks

---

## APIs Used

| API | Purpose | Endpoint |
|-----|---------|----------|
| Open Notify ISS | Get current ISS latitude/longitude | `http://api.open-notify.org/iss-now.json` |
| Sunrise-Sunset | Get sunrise/sunset for a location | `https://api.sunrise-sunset.org/json` |

Both APIs are **free** and require **no API key**.

---

## Authentication

This project uses **OAuth 2.0** to send emails via the Gmail API, not the
traditional `smtplib` + App Password approach. Google has deprecated
"Less Secure Apps" and App Passwords are now unreliable for many accounts.

The script uses:

- `credentials.json` — OAuth client credentials (Client ID + Secret)
- `token.json` — saved access & refresh tokens (created on first run)

Both files are **not committed to Git** (see `.gitignore`).

On the **first run**, a browser window opens for you to authorize the app.
On subsequent runs, the token refreshes silently.

---

## Project Structure
Day33-API-Endpoints-and-API-Parameters-ISS-Overhead-Notifier/
├── main.py # The main script
├── credentials.json # OAuth client credentials (not in Git)
├── token.json # Saved tokens (not in Git)
├── .gitignore # Excludes sensitive files
└── README.md # This file

text

---

## Setup

### 1. Install dependencies

```bash
pip install requests google-auth-oauthlib google-auth-httplib2 google-api-python-client
```
2. Get your location's coordinates
Use LatLong.net or Google Maps to find your
latitude and longitude, then update MY_LAT and MY_LONG in main.py.

3. Set up Gmail API credentials
Go to the Google Cloud Console.

Create a new project.

Enable the Gmail API.

Configure the OAuth consent screen (External, add yourself as a test user).

Create OAuth client ID credentials (Application type: Desktop app).

Download the JSON file, rename it to credentials.json, and place it
in the project folder.

4. Run the script
```bash
python main.py
```
On first run, a browser window will open for you to authorize the app.
After that, the script runs silently and checks every 60 seconds.

Notes
The Sunrise-Sunset API returns times in UTC by default. The script
extracts only the hour from these times, which is Angela's approach
and is accurate enough for this project.

The ±5° threshold means the ISS is considered "overhead" if it's within
5 degrees of your position in both latitude and longitude.

To stop the loop, press Ctrl + C in the terminal.

Acknowledgements
Project idea and structure from Dr. Angela Yu's 100 Days of Code course.
OAuth 2.0 integration adapted for Google's post-2025 Gmail API requirements.
