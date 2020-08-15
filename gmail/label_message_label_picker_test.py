import gmail_oo.label_messages_label_picker as picker
import gmail_oo.label_id_lookup as ll

label_lookup = ll.LabelIdLookup()
label_id1 = label_lookup.lookup('Jaco Koekemoer')
label_id2 = label_lookup.lookup('INBOX')

current_labels_ids = ['Test1','Test2',label_id1]
message_picker = picker.LabelMessagesLabelPicker()
message_picker.pick(current_labels_ids)

add_label_list = message_picker.get_add_label_ids()
delete_label_list = message_picker.get_delete_label_ids()

print("\nAdd list")
for item in add_label_list:
    print(item)

print("\nDelete list")
for item in delete_label_list:
    print(item)

if len(add_label_list) == 0 and len(delete_label_list) == 0:
    print("No label modification required.")