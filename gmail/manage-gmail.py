#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:50:07 2020

@author: jaco

https://developers.google.com/gmail/api/v1/reference/users/messages/get?apix_params=%7B%22userId%22%3A%22me%22%2C%22id%22%3A%221353d05ffe71f466%22%7D
"""

# List messages and loop
# Get a message
# output it
# Determine in which folder it is
# If in inbox, label it, or archive it

import json
import pprint
import base64
import email

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def retrieve_json():
    print("Retrieving")
    #Read file
    json_filename = "/home/jaco/python-data/gmail/gmail_messages.json"
    try:
        f = open(json_filename, 'r')
        json_raw_data = f.read()
        json_data = json.loads(json_raw_data)   
        return json_data
    except Exception:
        print("File could not be opened")

def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    #print('Message snippet: %s' % message['snippet'])

    return message
  except errors.HttpError as error:
    print('An error occurred: %s' % error)


def GetMimeMessage(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    #print('Message snippet: %s' % message['snippet'])

    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    mime_msg = email.message_from_string(str(msg_str))

    return mime_msg
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

def print_section_divider():
    print("==" * 20)

def main():
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
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_pickle_path, 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Read messages from file
    gmail_json = retrieve_json() # Returnes a list of dictionaries
    cnt = 1
    print('Total messages: ', len(gmail_json))
    for item in gmail_json: # For each dictionary
        msg_id = item["id"] # Get the id dictionary item
        print_section_divider()
        print(msg_id)
        print_section_divider()
        
        # Retrieve the Gmail message
        user_id='me'
        message = GetMessage(service, user_id, msg_id)
        payload = message['payload']
        headers = payload['headers']
        
        # Get message info
        subject = ""
        date_received = ""
        from_email = ""
        to_email = ""
        for header in headers:
            if header['name'] == "Subject":
                subject = header['value']
            if header['name'] == "From":
                from_email = header['value']
            if header['name'] == "Date":
                date_received = header['value']
            if header['name'] == "To":
                to_email = header['value']
        print(msg_id, from_email, to_email, date_received, subject)
        
        # Print message
        #print('Message snippet: %s' % message['snippet'])
        #pprint.pprint(message)
        
        # Limit to certain amount of messages
        if cnt == 1:
            break
        else:
            cnt += 1
    
    # For each message, retrieve the message and output
    
    

if __name__ == '__main__':
    main()