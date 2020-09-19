"""
@author: Jaco Koekemoer
@date: 2020-09-13

Using a previously stored list of messages ids, retrieve those message contents, and store them in a file.
"""
import gmail_oo.json_retriever as jr
import gmail_oo.gmail_connector as gc
import gmail_oo.get_message as gm
import gmail_oo.utils as u
import gmail_oo.json_saver as js
import time as t
import os.path as p

class StoreMessagesApp:

    def __init__(self, filename_str):
        self.filename_str = filename_str

    def run(self):
        # Message storage directory
        inbox_dir = "/home/jaco/python-data/gmail/inbox"

        # Read messages from file
        json_filename = "/home/jaco/python-data/gmail/gmail_messages_{}.json".format(self.filename_str)
        json_retriever = jr.JSONRetriever()
        gmail_json = json_retriever.retrieve(json_filename)  # Returnes a list of dictionaries
        cnt = 1
        print('Total messages: ', len(gmail_json))
        user_id = u.GmailEnum.USER_ID.value

        # Connect to GMail
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Instantiate object to call GMail API to get the message
        get_message = gm.GetMessage(service, user_id)

        # Prep and start the loop
        total = len(gmail_json)
        next_10_sec_sleep = 100
        interval_10_sec_sleep = 100
        current = 1
        for item in gmail_json:  # For each message in the JSON file
            u.print_section_divider()
            print("Processing {} of {}".format(current, total))
            current += 1
            #print(item)

            msg_id = item["id"]  # Get the id dictionary item
            storage_path = inbox_dir + "/" + msg_id
            if p.exists(storage_path):
                print("Message already stored: {}".format(msg_id))
                continue

            # Sleeping logic
            if  current == next_10_sec_sleep:
                print("Sleeping 10 seconds")
                t.sleep(10)
                next_10_sec_sleep += interval_10_sec_sleep
            else:
                print("Sleeping 1 seconds")
                t.sleep(1)

            # Retrieve the Gmail message
            print("Retrieving message {}".format(msg_id))
            message = get_message.get(msg_id)
            if message == None:
                print("Message ID {} not found".format(msg_id))
                continue
            #print(message)

            # Store the JSON message
            json_saver = js.JSONSaver()
            json_saver.save(storage_path, message)


if __name__ == '__main__':
    filename_str = "inbox"
    store_messages_app = StoreMessagesApp(filename_str)
    store_messages_app.run()
