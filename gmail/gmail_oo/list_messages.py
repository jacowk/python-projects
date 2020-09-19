"""
@author: Jaco Koekemoer
@date: 2020-08-28

List messages
"""
from datetime import datetime
import gmail_oo.gmail_connector as gc
import gmail_oo.list_messages_matching_query as lq
import gmail_oo.json_saver as js
import gmail_oo.utils as u
import os.path as p

class ListMessages:

    def __init__(self, filename_str, email_from):
        self.filename_str = filename_str
        self.email_from = email_from

    def run(self):
        current_date_time = datetime.today().strftime('%Y%m%d%H%M%S')
        json_filename = "/home/jaco/python-data/gmail/gmail_messages_{}.json".format(self.filename_str)

        print("List messages - Filename substring: {} - Email from: {}".format(self.filename_str, self.email_from))

        # Verify that the file does not exist
        if p.isfile(json_filename):
            print("File already exists {}. Aborting".format(json_filename))
            return

        query = "in:inbox from:{}".format(self.email_from)
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Call the Gmail API
        user_id = u.GmailEnum.USER_ID.value
        list_messages = lq.ListMessagesMatchingQuery(service, user_id, query)
        messages = list_messages.list()
        if not messages:
            print("No messages")
            return False
        else:
            json_saver = js.JSONSaver()
            json_saver.save(json_filename, messages)
            print(messages)
            print("Found {}".format(len(messages)))
            print("Now run label_messages_app.py to modify labels, or delete_messages_app.py to delete messages")
            return True
