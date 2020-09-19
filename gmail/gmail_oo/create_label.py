"""
@author: Jaco Koekemoer
@date: 2020-08-16

A class to create labels for GMail
"""
from apiclient import errors

class CreateLabel:

    def __init__(self, service, user_id):
        self.service = service
        self.user_id = user_id

    def create(self, label_name):
        """Creates a new label within user's mailbox, also prints Label ID.

        Args:
          service: Authorized Gmail API service instance.
          user_id: User's email address. The special value "me"
          can be used to indicate the authenticated user.
          label_object: label to be added.

        Returns:
          Created Label.
        """
        try:
            label = self.service.users().labels().create(userId=self.user_id,
                                                    body=self.make_label(label_name)).execute()
            print
            label['id']
            return label
        except errors.HttpError as error:
            print('An error occurred: {}'.format(error))

    def make_label(self, label_name, mlv='show', llv='labelShow'):
        """Create Label object.

        Args:
          label_name: The name of the Label.
          mlv: Message list visibility, show/hide.
          llv: Label list visibility, labelShow/labelHide.

        Returns:
          Created Label.
        """
        label = {'messageListVisibility': mlv,
                 'name': label_name,
                 'labelListVisibility': llv}
        return label
