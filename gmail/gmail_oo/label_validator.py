"""
@author: Jaco Koekemoer
@date: 2020-08-30

"""
import gmail_oo.label_id_lookup as ll
import create_label_app as cla
import store_labels_app as sla
import gmail_oo.utils as u

class LabelValidator:

    def __init__(self, relabel_list):
        self.relabel_list = relabel_list

    def validate(self):
        # Validate that the lookup exists
        label_lookup = ll.LabelIdLookup()

        # Determine which label ids to add
        for list_item_key in self.relabel_list.keys():
            filename_str = list_item_key
            label_name = self.relabel_list[list_item_key][0]
            email_from = self.relabel_list[list_item_key][1]
            add_label_id = label_lookup.lookup(label_name)
            if add_label_id == None:
                if u.confirmation("Label {} does not exist. Do you want to create it?".format(label_name)):
                    create_label_app = cla.CreateLabelApp(label_name=label_name)
                    create_label_app.run()
                else:
                    raise Exception("Label {} not found. Add it with create_label_app.py")

        store_labels_app = sla.StoreLabelsApp()
        store_labels_app.run()

if __name__ == '__main__':
    label_validator = LabelValidator(u.GmailEnum.RELABEL_LIST.value)
    label_validator.validate()