"""
@author: Jaco Koekemoer
@date: 2020-08-15

https://developers.google.com/gmail/api/v1/reference/users/labels/get
"""
from apiclient import errors

class GetLabel:

    def __init__(self, service, user_id):
        self.service = service
        self.user_id = user_id

    def get(self, label_id):
        try:
            label = self.service.users().labels().get(userId=self.user_id, id=label_id).execute()
            return label
        except errors.HttpError as error:
            print('An error occurred: {}'.format(error))