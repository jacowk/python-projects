"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
from apiclient import errors

class DeleteMessage:

    def __init__(self, service, user_id):
        self.service = service
        self.user_id = user_id

    def delete(self, msg_id):
        """Delete a Message.

          Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            msg_id: ID of Message to delete.
          """
        try:
            self.service.users().messages().delete(userId=self.user_id, id=msg_id).execute()
            print('Message with id: %s deleted successfully.' % msg_id)
        except errors.HttpError as error:
            print('An error occurred: %s' % error)