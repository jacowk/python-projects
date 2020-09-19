"""
@author: Jaco Koekemoer
@date: 2020-08-14

Given a list of messages, delete each message.
The list of messages is created using list_messages_query_app.py
"""
import gmail_oo.gmail_connector as gc
import gmail_oo.json_retriever as jr
import gmail_oo.get_message as gm
import gmail_oo.delete_message as dm
import gmail_oo.utils as u
import pprint
import time as t

class DeleteMessagesApp:

    def print_section_divider(self):
        print("==" * 20)

    def run(self):
        print("Before running this app, make sure you ran list_messages_query_app.py to get the messages to delete.")
        if not u.confirmation("Do you want to continue deleting the messages?"):
            return

        filename_str = u.GmailEnum.FILENAME_SUBSTRING.value
        email_from = u.GmailEnum.EMAIL_FROM.value

        print("Delete messages - Filename substring: {} - Email from: {}".format(filename_str, email_from))

        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Read messages from file
        json_filename = "/home/jaco/python-data/gmail/gmail_messages_{}.json".format(filename_str)
        json_retriever = jr.JSONRetriever()
        gmail_json = json_retriever.retrieve(json_filename)  # Returnes a list of dictionaries
        cnt = 1
        print('Total messages: ', len(gmail_json))
        user_id = u.GmailEnum.USER_ID.value
        get_message = gm.GetMessage(service, user_id)
        delete_message = dm.DeleteMessage(service, user_id)
        total = len(gmail_json)
        current = 1
        for item in gmail_json:  # For each dictionary
            self.print_section_divider()
            print("Processing {} of {}".format(current, total))
            current += 1
            msg_id = item["id"]  # Get the id dictionary item

            # Retrieve the Gmail message
            message = get_message.get(msg_id)
            if message == None:
                print("Message ID {} not found".format(msg_id))
                continue
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

            # Delete selected message
            if email_from in from_email:
                print("Deleting " + msg_id)
                delete_message.delete(msg_id)

            # Print message
            #print('Message snippet: %s' % message['snippet'])
            #pprint.pprint(message)

            # Limit to certain amount of messages
            #if cnt == 5:
            #    break
            #else:
            #    cnt += 1

            #Sleep 1 second
            print("Sleeping 1 sec")
            t.sleep(2)

if __name__ == '__main__':
    delete_messages_app = DeleteMessagesApp()
    delete_messages_app.run()