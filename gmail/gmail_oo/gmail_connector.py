"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GMailConnector:

    def connect(self):
        # If modifying these scopes, delete the file token.pickle.
        #scopes = ['https://www.googleapis.com/auth/gmail.readonly']
        scopes = ['https://mail.google.com/'] #Use this scope to delete messages

        """Shows basic usage of the Gmail API.
            Lists the user's Gmail labels.
            """
        token_pickle_path = "/home/jaco/python-data/gmail/token.pickle"
        credentials_path = "/home/jaco/python-data/gmail/credentials.json"

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(token_pickle_path):
            with open(token_pickle_path, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_pickle_path, 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)
        return service