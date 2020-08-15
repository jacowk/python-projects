"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
from apiclient import errors

class GetMessage:

    def __init__(self, service, user_id):
        self.service = service
        self.user_id = user_id

    def get(self, msg_id):
        """Get a Message with given ID.

          Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            msg_id: The ID of the Message required.

          Returns:
            A Message.
          """
        try:
            message = self.service.users().messages().get(userId=self.user_id, id=msg_id).execute()

            # print('Message snippet: %s' % message['snippet'])

            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)