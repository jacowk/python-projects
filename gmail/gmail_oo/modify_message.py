"""
@author: Jaco Koekemoer
@date: 2020-08-15

Given a message, modify the labels on the message

https://developers.google.com/gmail/api/v1/reference/users/messages/modify
"""
from apiclient import errors

class ModifyMessage:

    def __init__(self, service, user_id):
        self.service = service
        self.user_id = user_id

    def modify(self, msg_id, add_label_list, delete_label_list):
        """Modify the Labels on the given Message.

          Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            msg_id: The id of the message required.
            msg_labels: The change in labels.

          Returns:
            Modified message, containing updated labelIds, id and threadId.
          """
        try:
            message = self.service.users().messages().modify(userId=self.user_id, id=msg_id,
                                                        body=self.create_msg_labels(add_label_list, delete_label_list)).execute()

            label_ids = message['labelIds']

            print('Message ID: {} - With Label IDs {}'.format(msg_id, label_ids))
            return message
        except errors.HttpError as error:
            print('An error occurred: {}'.format(error))

    def create_msg_labels(self, add_label_list, delete_label_list):
        """Create object to update labels.

        Returns:
          A label update object.
        """
        #Also remove the message from inbox
        return {'removeLabelIds': delete_label_list, 'addLabelIds': add_label_list}
