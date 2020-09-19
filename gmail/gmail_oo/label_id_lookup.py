"""
@author: Jaco Koekemoer
@date: 2020-08-15

Lookup a gmail label_id, stored in a JSON file, that was initially retrieved with list_labels.py
"""
import gmail_oo.json_retriever as jr
import gmail_oo.utils as u

class LabelIdLookup:

    def lookup(self, label_name):
        # Retrieve local labels from JSON
        filename = u.GmailEnum.LABELS_FILE.value
        json_retriever = jr.JSONRetriever()
        labels_json = json_retriever.retrieve(filename)

        # Lookup label_id
        label_id = ''
        for label_json in labels_json:
            if label_json['name'] == label_name:
                label_id = label_json['id']
                break

        if len(label_id) == 0:
            print("Label ID for name {} not found".format(label_name))
            return None

        print("Label ID found: {}".format(label_id))
        return label_id
