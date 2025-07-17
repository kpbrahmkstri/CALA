import datetime
import os.path
import pytz
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Read-only access
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Set your local timezone
TIMEZONE = "America/Los_Angeles"  # Change if you're in a different region

def fetch_calendar_events():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Use timezone-aware datetime
    local_tz = pytz.timezone(TIMEZONE)
    now = datetime.datetime.now(local_tz)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=0)

    time_min = start_of_day.isoformat()
    time_max = end_of_day.isoformat()

    events_result = service.events().list(
        calendarId='primary',
        timeMin=time_min,
        timeMax=time_max,
        maxResults=20,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    structured_events = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        structured_events.append({
            "time": start,
            "title": event.get("summary", "No Title")
        })

    return {
        "today": {
            "meetings": structured_events
        }
    }