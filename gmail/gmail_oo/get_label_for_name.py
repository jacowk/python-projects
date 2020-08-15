"""
@author: Jaco Koekemoer
@date: 2020-08-15

Given a label name, retrieve that label from GMail
"""
import gmail_oo.get_label as gl
import gmail_oo.label_id_lookup as ll

class GetLabelForName:

    def __init__(self, service, user_id):
        self.service = service
        self.user_id = user_id

    def get(self, label_name):
        # Retrieve local labels from JSON
        label_id_lookup = ll.LabelIdLookup()
        label_id = label_id_lookup.lookup(label_name)

        # Retrieve the label from GMail
        get_label = gl.GetLabel(self.service, self.user_id)
        label = get_label.get(label_id)
        return label