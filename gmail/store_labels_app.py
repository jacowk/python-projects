"""
@author: Jaco Koekemoer
@date: 2020-08-15
"""
import gmail_oo.gmail_connector as gc
import gmail_oo.list_labels as ll
import gmail_oo.json_saver as js
import gmail_oo.utils as u

class StoreLabelsApp:

    def run(self):
        # Connect to GMail
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        # List the labels
        user_id = 'me'
        list_labels = ll.ListLabels(service, user_id)
        labels = list_labels.list()

        # Print the labels
        print(labels)

        # Store JSON
        filename = u.GmailEnum.LABELS_FILE.value
        jason_saver = js.JSONSaver()
        jason_saver.save(filename, labels)

if __name__ == '__main__':
    store_labels_app = StoreLabelsApp()
    store_labels_app.run()