"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
from apiclient import errors

class ListMessagesMatchingQuery:

    def __init__(self, service, user_id, query=''):
        self.service = service
        self.user_id = user_id
        self.query = query

    def list(self):
        """List all Messages of the user's mailbox matching the query.

          Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            query: String used to filter messages returned.
            Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

          Returns:
            List of Messages that match the criteria of the query. Note that the
            returned list contains Message IDs, you must use get with the
            appropriate ID to get the details of a Message.
          """
        try:
            response = self.service.users().messages().list(userId=self.user_id,
                                                       q=self.query).execute()
            messages = []
            if 'messages' in response:
                messages.extend(response['messages'])

            while 'nextPageToken' in response:
                page_token = response['nextPageToken']
                response = self.service.users().messages().list(userId=self.user_id, q=self.query,
                                                           pageToken=page_token).execute()
                messages.extend(response['messages'])

            return messages
        except errors.HttpError as error:
            print('An error occurred: %s' % error)