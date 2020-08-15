"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
from apiclient import errors
import base64
import email

class GetMimeMessage:

    def __init__(self, service, user_id):
        self.service = service
        self.user_id = user_id

    def get(self, msg_id):
        """Get a Message and use it to create a MIME Message.

          Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            msg_id: The ID of the Message required.

          Returns:
            A MIME Message, consisting of data from Message.
          """
        try:
            message = self.service.users().messages().get(userId=self.user_id, id=msg_id,
                                                     format='raw').execute()

            # print('Message snippet: %s' % message['snippet'])

            msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

            mime_msg = email.message_from_string(str(msg_str))

            return mime_msg
        except errors.HttpError as error:
            print('An error occurred: %s' % error)