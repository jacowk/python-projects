"""
@author: Jaco Koekemoer
@date: 2020-08-28
"""

import gmail_oo.gmail_connector as gc
import gmail_oo.utils as u
import gmail_oo.modify_message as mm
import gmail_oo.label_messages_label_picker as picker

class LabelSingleMessage:

    def __init__(self, message, email_from, add_labels=u.GmailEnum.ADD_LABEL_NAMES.value, delete_labels=u.GmailEnum.DELETE_LABEL_NAMES.value):
        self.message = message
        self.email_from = email_from
        self.add_labels = add_labels
        self.delete_labels = delete_labels

    def print_section_divider(self):
        print("==" * 20)

    def run(self):
        msg_id = self.message["id"]

        print("Label messages - Message ID: {} - Email from: {}".format(msg_id, self.email_from))

        # Connect to GMail
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()
        user_id = u.GmailEnum.USER_ID.value

        # Instantiate object to call GMail API to modify the message labels
        modify_message = mm.ModifyMessage(service, user_id)

        if self.message == None:
            print("Message was emtpy")
            return

        payload = self.message['payload']
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
        print("Label IDs: {}".format(self.message['labelIds']))

        # Pick labels to add and delete
        message_picker = picker.LabelMessagesLabelPicker(self.add_labels, self.delete_labels)
        message_picker.pick(self.message['labelIds'])
        add_label_list = message_picker.get_add_label_ids()
        delete_label_list = message_picker.get_delete_label_ids()

        print("Add Labels")
        print (add_label_list)
        print("Delete Labels")
        print(delete_label_list)

        # if there are no labels, then continue
        if len(add_label_list) == 0 and len(delete_label_list) == 0:
            print("No label modification required. Continue.")
            return

        # Don't label if label to add is None
        if None in add_label_list:
            u.confirmation("None label in add_label_list".format(self.label_name))
            return

        # If not, assign the label to the message
        if self.email_from in from_email or self.email_from == from_email:
            print("Modifying message id {}".format(msg_id))
            modify_message.modify(msg_id, add_label_list, delete_label_list)
        else:
            print("{} not in {}".format(self.email_from, from_email))