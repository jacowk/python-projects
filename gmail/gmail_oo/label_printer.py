"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
class LabelPrinter:

    def __init__(self, service):
        self.service = service

    def print(self):
        # Call the Gmail API
        results = self.service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])