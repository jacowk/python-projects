"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
from apiclient import errors

class ListMessagesWithLabels:

    def __init__(self, service, user_id, label_ids=[]):
        self.service = service
        self.user_id = user_id
        self.label_ids = label_ids

    def list(self):
        """List all Messages of the user's mailbox with label_ids applied.

          Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            label_ids: Only return Messages with these labelIds applied.

          Returns:
            List of Messages that have all required Labels applied. Note that the
            returned list contains Message IDs, you must use get with the
            appropriate id to get the details of a Message.
          """
        try:
            response = self.service.users().messages().list(userId=self.user_id,
                                                       labelIds=self.label_ids).execute()
            messages = []
            if 'messages' in response:
                messages.extend(response['messages'])

            while 'nextPageToken' in response:
                page_token = response['nextPageToken']
                response = self.service.users().messages().list(userId=self.user_id,
                                                           labelIds=self.label_ids,
                                                           pageToken=page_token).execute()
                messages.extend(response['messages'])

            return messages
        except errors.HttpError as error:
            print('An error occurred: %s' % error)