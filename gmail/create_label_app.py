"""
@author: Jaco Koekemoer
@date: 2020-08-16

An app class to create labels for GMail
"""
import gmail_oo.gmail_connector as gc
import gmail_oo.create_label as cl
import gmail_oo.utils as u
import gmail_oo.label_id_lookup as ll

class CreateLabelApp:

    def __init__(self, label_name=u.GmailEnum.LABEL_NAME.value):
        self.label_name = label_name

    def run(self):
        # Connect to GMail
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # Check if the label exists
        # Retrieve local labels from JSON
        label_id_lookup = ll.LabelIdLookup()
        label_id = label_id_lookup.lookup(self.label_name)
        if label_id != None:
            print("Label already exists, aborting")
            return

        # Create the new label
        print("Creating label {}".format(self.label_name))
        create_label = cl.CreateLabel(service, u.GmailEnum.USER_ID.value)
        create_label.create(self.label_name)

        print("Done. Remember to rerun store_labels_app.py to refresh local labels")


if __name__ == '__main__':
    create_label_app = CreateLabelApp()
    create_label_app.run()
