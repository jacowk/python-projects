"""
@author: Jaco Koekemoer
@date: 2020-08-15

Given a list of messages, label each message with a specific label.
The list of messages is created using list_messages_query_app.py
"""
import gmail_oo.gmail_connector as gc
import gmail_oo.json_retriever as jr
import gmail_oo.get_message as gm
import gmail_oo.utils as u
import gmail_oo.modify_message as mm
import gmail_oo.label_id_lookup as ll
import gmail_oo.label_messages_label_picker as picker
import pprint
import time as t

class LabelMessagesApp:

    def print_section_divider(self):
        print("==" * 20)

    def run(self):
        print("Before running this app, make sure you ran list_messages_query_app.py to get the messages to label.")
        if not u.confirmation("Do you want to continue labeling the messages?"):
            return

        filename_str = u.GmailEnum.FILENAME_SUBSTRING.value
        email_from = u.GmailEnum.EMAIL_FROM.value

        print("Label messages - Filename substring: {} - Email from: {}".format(filename_str, email_from))

        # Connect to GMail
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Read messages from file
        json_filename = "/home/jaco/python-data/gmail/gmail_messages_{}.json".format(filename_str)
        json_retriever = jr.JSONRetriever()
        gmail_json = json_retriever.retrieve(json_filename)  # Returnes a list of dictionaries
        cnt = 1
        print('Total messages: ', len(gmail_json))
        user_id = u.GmailEnum.USER_ID.value

        # Instantiate object to call GMail API to get the message
        get_message = gm.GetMessage(service, user_id)

        # Instantiate object to call GMail API to modify the message labels
        modify_message = mm.ModifyMessage(service, user_id)

        # Prep and start the loop
        total = len(gmail_json)
        current = 1
        for item in gmail_json:  # For each message in the JSON file
            print("Sleeping 1 seconds")
            t.sleep(1)
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
            print("Header Info: ", msg_id, from_email, to_email, date_received, subject)
            print("Label IDs: {}".format(message['labelIds']))

            # Pick labels to add and delete
            message_picker = picker.LabelMessagesLabelPicker()
            message_picker.pick(message['labelIds'])
            add_label_list = message_picker.get_add_label_ids()
            delete_label_list = message_picker.get_delete_label_ids()

            print("Add Labels")
            print (add_label_list)
            print("Delete Labels")
            print(delete_label_list)

            # if there are no labels, then continue
            if len(add_label_list) == 0 and len(delete_label_list) == 0:
                print("No label modification required. Continue.")
                continue

            # If not, assign the label to the message
            if email_from in from_email or email_from == from_email:
                print("Modifying message id {}".format(msg_id))
                modify_message.modify(msg_id, add_label_list, delete_label_list)
            else:
                print("{} not in {}".format(email_from, from_email))

            # Limit to certain amount of messages
            #if cnt == 1:
            #    break
            #else:
            #    cnt += 1

if __name__ == '__main__':
    label_message_app = LabelMessagesApp()
    label_message_app.run()
