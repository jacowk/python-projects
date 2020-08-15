"""
@author: Jaco Koekemoer
@date: 2020-08-15
"""
import gmail_oo.json_retriever as jr
import gmail_oo.utils as u

class ListLocalJSONLabels:

    def list(self):
        # Retrieve local labels from JSON
        filename = u.GmailEnum.LABELS_FILE.value
        json_retriever = jr.JSONRetriever()
        labels_json = json_retriever.retrieve(filename)

        # Print labels
        for label_json in labels_json:
            for key in label_json.keys():
                print("{}: {}".format(key, label_json[key]))
            print("\n")