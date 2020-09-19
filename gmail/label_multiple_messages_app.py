"""
@author: Jaco Koekemoer
@date: 2020-08-28

Using constants from utils.py, loop through a list of email addresses, remove them from
inbox, and place them in the label specified in the utils.py enum.
"""
import gmail_oo.label_messages as lm
import gmail_oo.list_messages as listm
import gmail_oo.label_validator as lv
import gmail_oo.utils as u

class LabelMultipleMessagesApp:

    def __init__(self, relabel_list):
        self.relabel_list = relabel_list

    def run(self):
        # Validate if a label exists
        label_validator = lv.LabelValidator(relabel_list)
        label_validator.validate()

        # Get the configs from utils and start the loop
        for list_item_key in self.relabel_list.keys():
            filename_str = list_item_key
            label_name = self.relabel_list[list_item_key][0]
            email_from = self.relabel_list[list_item_key][1]
            add_labels = [ label_name ]
            print("Processing {}, {}, {}".format(filename_str, label_name, email_from))

            # List the messages
            list_messages = listm.ListMessages(filename_str, email_from)
            result = list_messages.run()
            if result:
                # Start to relabel all the messages
                label_messages = lm.LabelMessages(filename_str, email_from, add_labels=add_labels)
                label_messages.run()

if __name__ == '__main__':
    relabel_list = u.GmailEnum.RELABEL_LIST.value
    label_multiple_message_app = LabelMultipleMessagesApp(relabel_list)
    label_multiple_message_app.run()
