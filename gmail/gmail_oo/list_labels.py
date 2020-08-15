"""
@author: Jaco Koekemoer
@date: 2020-08-15
"""
from apiclient import errors

class ListLabels:

    def __init__(self, service, user_id):
        self.service = service
        self.user_id = user_id

    def list(self):
        """Get a list all labels in the user's mailbox.

         Args:
           service: Authorized Gmail API service instance.
           user_id: User's email address. The special value "me"
           can be used to indicate the authenticated user.

         Returns:
           A list all Labels in the user's mailbox.
         """
        try:
            response = self.service.users().labels().list(userId=self.user_id).execute()
            labels = response['labels']
            for label in labels:
                print('Label id: {} - Label name: {}'.format(label['id'], label['name']))
            return labels
        except errors.HttpError as error:
            print('An error occurred: {}'.format(error))