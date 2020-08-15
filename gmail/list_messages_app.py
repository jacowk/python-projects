#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:12:08 2020

@author: jaco

Get a list of Messages from the user's mailbox.
"""

from __future__ import print_function
import gmail_oo.gmail_connector as gc
import gmail_oo.list_messages_with_labels as lm
import gmail_oo.json_saver as js

class ListMessagesApp:

    def run(self):
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Call the Gmail API
        list_messages = lm.ListMessagesWithLabels(service, user_id='me', label_ids=['INBOX'])
        messages = list_messages.list()
        if not messages:
            print("No messages")
        else:
            json_filename = "/home/jaco/python-data/gmail/gmail_messages.json"
            json_saver = js.JSONSaver()
            json_saver.save(json_filename, messages)
            print(messages)

if __name__ == '__main__':
    list_messages_app = ListMessagesApp()
    list_messages_app.list()

