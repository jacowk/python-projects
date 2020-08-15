"""
@author: Jaco Koekemoer
@date: 2020-08-15

Get a message and print it
"""
import gmail_oo.gmail_connector as gc
import gmail_oo.json_retriever as jr
import gmail_oo.get_message as gm
import gmail_oo.delete_message as dm
import gmail_oo.utils as u
import pprint
import time as t

class GetMessageApp:

    def print_section_divider(self):
        print("==" * 20)

    def run(self):
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Read messages from file
        json_filename = "/home/jaco/python-data/gmail/gmail_messages.json"
        json_retriever = jr.JSONRetriever()
        gmail_json = json_retriever.retrieve(json_filename)  # Returnes a list of dictionaries
        cnt = 1
        print('Total messages: ', len(gmail_json))
        user_id = 'me'
        get_message = gm.GetMessage(service, user_id)
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
            print("Header Info: ", msg_id, from_email, to_email, date_received, subject)

            # Print message
            print('Message snippet: %s' % message['snippet'])
            print("Label IDs: {}".format(message['labelIds']))

            #pprint.pprint(message)

            # Limit to certain amount of messages
            if cnt == 1:
                break
            else:
                cnt += 1

            #Sleep 1 second
            print("Sleeping 1 sec")
            t.sleep(2)

if __name__ == '__main__':
    get_message_app = GetMessageApp()
    get_message_app.run()