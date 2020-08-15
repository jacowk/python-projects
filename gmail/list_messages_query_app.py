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

class ListMessagesQueryApp:

    def run(self):
        filename_str = u.GmailEnum.FILENAME_SUBSTRING.value
        email_from = u.GmailEnum.EMAIL_FROM.value

        query = "from:{}".format(email_from)
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Call the Gmail API
        user_id = 'me'
        list_messages = lq.ListMessagesMatchingQuery(service, user_id, query)
        messages = list_messages.list()
        if not messages:
            print("No messages")
        else:
            json_filename = "/home/jaco/python-data/gmail/gmail_messages_{}.json".format(filename_str)
            json_saver = js.JSONSaver()
            json_saver.save(json_filename, messages)
            print(messages)
            print("Found {}".format(len(messages)))

if __name__ == '__main__':
    list_messages_app = ListMessagesQueryApp()
    list_messages_app.run()

