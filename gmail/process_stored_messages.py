"""
@author: Jaco Koekemoer
@date: 2020-09-19

Read message JSON from inbox_analysis.json, and process it.
"""
import csv
import gmail_oo.json_retriever as jr
import os.path as path
import gmail_oo.delete_message as dm
import gmail_oo.utils as u
import gmail_oo.gmail_connector as gc
import gmail_oo.label_messages as lm
import gmail_oo.single_label_validator as lv

class ProcessStoredMessagesApp:

    def __init__(self, json_filepath, csv_filepath, inbox_path):
        self.json_filepath = json_filepath
        self.csv_filepath = csv_filepath
        self.inbox_path = inbox_path

    def run(self):
        print("Filepath: {}".format(self.json_filepath))

        # Read JSON File
        json_retriever = jr.JSONRetriever()
        json_messages = json_retriever.retrieve(self.json_filepath)

        # Create GMail connector
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()
        user_id = u.GmailEnum.USER_ID.value

        # Read CSV file
        # Import csv
        with open(self.csv_filepath, newline='') as csvfile:

            datareader = csv.reader(csvfile, delimiter=',')
            cnt = 1

            for row in datareader:
                if cnt == 1:
                    cnt += 1
                    continue  # Skip first line with only column names

                email_address = row[0]
                email_count = row[1]
                label_name = row[2]
                print("=" * 10)
                print("\nProcessing {}, {}, {}".format(email_address, email_count, label_name))

                # Get the list of JSON messages
                messages = json_messages[email_address]
                #print(messages)

                if label_name == "skip":
                    print("Skipping")
                    continue

                # Read messages from file
                for message_id in messages:
                    process_file = "{}{}".format(self.inbox_path, message_id)
                    if path.exists(process_file):
                        # Parse JSON
                        json_retriever = jr.JSONRetriever()
                        message = json_retriever.retrieve(process_file)

                        #If delete, then delete the message
                        if label_name == "delete":
                            print("Deleting message {}".format(message_id))
                            delete_message = dm.DeleteMessage(service, user_id)
                            delete_message.delete(message_id)
                        else:
                            # Validate if a label exists
                            label_validator = lv.SingleLabelValidator(label_name)
                            label_validator.validate()

                            #Label the message
                            print("Labeling message {}".format(message_id))
                            add_labels = [label_name]
                            label_messages = lm.LabelMessages(process_file, email_address, add_labels=add_labels)
                            label_messages.run()



        # Loop through JSON file
        """
        for key in message_json.keys():
            print("Messages for {}".format(key))
            message_ids = message_json[key]
            for message_id in message_ids:
                print(message_id)
        """

        #print(message_json)

if __name__ == '__main__':
    json_filepath = "/home/jaco/python-data/gmail/inbox_analysis.json"
    csv_filepath = "/home/jaco/python-data/gmail/inbox_analysis_labels.csv"
    inbox_path = "/home/jaco/python-data/gmail/inbox/"
    app = ProcessStoredMessagesApp(json_filepath, csv_filepath, inbox_path)
    app.run()

