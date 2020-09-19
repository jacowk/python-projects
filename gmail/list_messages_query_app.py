#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:12:08 2020

@author: jaco

Get a list of Messages from the user's mailbox.
"""

from __future__ import print_function
import gmail_oo.gmail_connector as gc
import gmail_oo.list_messages_matching_query as lq
import gmail_oo.json_saver as js
import gmail_oo.utils as u
import os.path as p

class ListMessagesQueryApp:

    def run(self):
        #filename_str = u.GmailEnum.FILENAME_SUBSTRING.value
        filename_str = "inbox"
        email_from = u.GmailEnum.EMAIL_FROM.value
        json_filename = "/home/jaco/python-data/gmail/gmail_messages_{}.json".format(filename_str)

        #print("List messages - Filename substring: {} - Email from: {}".format(filename_str, email_from))

        # Verify that the file does not exist
        if p.isfile(json_filename):
            print("File already exists {}. Aborting".format(json_filename))
            return

        #query = "in:inbox from:{}".format(email_from)
        query = "in:inbox"
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Call the Gmail API
        user_id = u.GmailEnum.USER_ID.value
        list_messages = lq.ListMessagesMatchingQuery(service, user_id, query)
        messages = list_messages.list()
        if not messages:
            print("No messages")
        else:
            json_saver = js.JSONSaver()
            json_saver.save(json_filename, messages)
            print(messages)
            print("Found {}".format(len(messages)))
            print("Now run label_messages_app.py to modify labels, or delete_messages_app.py to delete messages")

if __name__ == '__main__':
    list_messages_app = ListMessagesQueryApp()
    list_messages_app.run()

