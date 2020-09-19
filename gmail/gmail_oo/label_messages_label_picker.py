"""
@author: Jaco Koekemoer
@date: 2020-08-15

Determined which labels to add, and which labels to remove, based on the current list of labels for a message.
"""
import gmail_oo.label_id_lookup as ll

class LabelMessagesLabelPicker:

    add_label_ids = list()  # The final list of label ids to add
    delete_label_ids = list()  # The final list of label ids to remove

    def __init__(self, add_labels, delete_labels):
        self.add_labels = add_labels
        self.delete_labels = delete_labels

    def pick(self, current_label_ids):
        self.add_label_ids.clear()
        self.delete_label_ids.clear()

        label_lookup = ll.LabelIdLookup()

        # Determine which label ids to add
        for add_label_name in self.add_labels:
            add_label_id = label_lookup.lookup(add_label_name)
            if add_label_id not in current_label_ids:
                self.add_label_ids.append(add_label_id)

        # Determine which label ids to remove
        for delete_label_name in self.delete_labels:
            delete_label_id = label_lookup.lookup(delete_label_name)
            if delete_label_id in current_label_ids:
                self.delete_label_ids.append(delete_label_id)


    def get_add_label_ids(self):
        return self.add_label_ids

    def get_delete_label_ids(self):
        return self.delete_label_ids