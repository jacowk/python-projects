"""
@author: Jaco Koekemoer
@date: 2020-09-14

Get a single message and print it
"""
import gmail_oo.gmail_connector as gc
import gmail_oo.get_message as gm

class GetSingleMessageApp:

    def __init__(self, msg_id):
        self.msg_id = msg_id

    def print_section_divider(self):
        print("==" * 20)

    def run(self):
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Read messages from file
        user_id = 'me'
        get_message = gm.GetMessage(service, user_id)

        # Retrieve the Gmail message
        message = get_message.get(self.msg_id)
        if message == None:
            print("Message ID {} not found".format(self.msg_id))
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
        print("Header Info: ", self.msg_id, from_email, to_email, date_received, subject)

        # Print message
        print('Message snippet: %s' % message['snippet'])
        print("Label IDs: {}".format(message['labelIds']))

        #pprint.pprint(message)

if __name__ == '__main__':
    message_id = "1743174990b6f8fe"
    get_single_message_app = GetSingleMessageApp(message_id)
    get_single_message_app.run()