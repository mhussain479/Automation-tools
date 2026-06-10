import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://mail.google.com/"]


def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    target_email = input("Enter your target email here:")
    query = f"from:{target_email}"
    messages = []
    page_token = None
    
    while True:
        results = service.users().messages().list(
            userId="me", 
            q=query, 
            pageToken=page_token
        ).execute()
        
        batch = results.get("messages", [])
        if batch:
            messages.extend(batch)
            print(f"[*] Found {len(messages)} so far...")
        
        page_token = results.get("nextPageToken")
        if not page_token:
            break
    if not messages:
      print(f"No emails found from {target_email}")
    
    else:
      print(f"Found {len(messages)} email(s) from {target_email}")
    confirm = input("Delete these emails? (yes/no): ")
    if confirm.lower() == "yes":
        print("Deleting...")
        for message in messages:
          msg_id = message["id"]
          service.users().messages().trash(userId="me", id=msg_id).execute()
        print(f"Deleted {len(messages)} email(s).")
    else:
        print("Cancelled.")

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()