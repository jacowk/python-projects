"""
@author: Jaco Koekemoer
@date: 2020-08-30

"""
import gmail_oo.label_id_lookup as ll
import create_label_app as cla
import store_labels_app as sla
import gmail_oo.utils as u

class SingleLabelValidator:

    def __init__(self, label_name):
        self.label_name = label_name

    def validate(self):
        # Validate that the lookup exists
        label_lookup = ll.LabelIdLookup()

        # Determine which label ids to add
        add_label_id = label_lookup.lookup(self.label_name)
        if add_label_id == None:
            if u.confirmation("Label {} does not exist. Do you want to create it?".format(self.label_name)):
                create_label_app = cla.CreateLabelApp(label_name=self.label_name)
                create_label_app.run()

                store_labels_app = sla.StoreLabelsApp()
                store_labels_app.run()
            else:
                raise Exception("Label {} not found. Add it with create_label_app.py")


if __name__ == '__main__':
    label_validator = SingleLabelValidator(u.GmailEnum.RELABEL_LIST.value)
    label_validator.validate()